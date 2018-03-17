import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import quandl
import pandas as pd
import datetime
from plots import figure1, figure5
quandl.ApiConfig.api_key = ''


app = dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

df = quandl.get("FRED/GDP")
df= df.reset_index()
df['Date']=pd.to_datetime(df.Date.values)
df['Date']=df["Date"].apply(lambda x: x.year)
unique_years = df.Date.unique()

app.layout = html.Div([

# First row
html.Div([
        html.H2(
            children='Homework 5',
            style={'color':'#230156', 'fontFamily':'Comic Sans MS', 'textAlign': 'center', 'fontWeight':'bold'}),
        ], className='row'),
#Second row
html.Div([
        #Radio button
        html.Div([
		dcc.RadioItems(
		id='option_in1',
    	options=[
        {'label':"Employee Churn", 'value':'figure1'},
        {'label':'Startup RoadMap','value':'figure5'}
	   ],
        value='figure1')
	   ],className='four columns'),
        html.Div([
		html.Div(id='output')
	   ],className='eight columns') 
], className='row'),

#Third row
html.Div([
            html.Div([dcc.Dropdown(
            id='option_in2',
            options=[
            {'label': 'Google', 'value': 'GOOGL'},
            {'label': 'Apple', 'value': 'AAPL'},
            {'label': 'TESLA', 'value': 'TSLA'},
            {'label': 'Amazon', 'value': 'AMZN'},
            {'label': 'IBM', 'value': 'IBM'},
            ],
            multi=True,
            value=['GOOGL', 'IBM'],
            placeholder= "Please, select a stock" ),
            html.Button(id='submit', n_clicks=0, children='Submit')
            ], className='three columns'),

        html.Div([dcc.Graph(id='figure3')], className='six columns'),
        html.Div([dcc.Graph(id='figure4')],className='three columns')
    ], className='row'),

#Fourth row-RangeSlider
html.Div([
    dcc.Graph(id='figure'),
    html.Div(
        dcc.RangeSlider(
            id='year-slider',
            min=unique_years[0],
            max=unique_years[-1],
            value=[unique_years[0], unique_years[-1]],
            marks={str(year): str(year) for year in df['Date'].unique()[::2]}
        ),
        style={'padding': '0px 60px'}
    )
],className='row')

], className='row')


#Radio-plots
@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='option_in1', component_property='value')]
)

def update_graph_1(selected_values):
    graphs=[]
    if 'figure1' in selected_values:
        graphs.append(html.Div(dcc.Graph(id='figure1', figure=figure1))),

    if 'figure5' in selected_values:
        graphs.append(html.Div(dcc.Graph(id='figure5', figure=figure5))) 
    return graphs

#Dropdown-plots
@app.callback(
    Output(component_id='figure3', component_property='figure'),
    [Input(component_id='submit', component_property='n_clicks')],
    [State(component_id='option_in2', component_property='value')],
)

def update_graph_2(clicks, input_value):
    input1 = "WIKI/" + input_value[0]
    data1 = quandl.get(input1)

    input2 = "WIKI/" + input_value[1]
    data2 = quandl.get(input2)

    trace1=go.Box(x=data1.Open.pct_change(), name=input_value[0])
    trace2=go.Box(x=data2.Open.pct_change(), name=input_value[1])
    layout3 = dict(title = "<i>Distribution of Price change</i>")
    data1 = [trace1, trace2]
    figure1 = dict(data=data1, layout=layout3)
    return figure1

@app.callback(
    Output(component_id='figure4', component_property='figure'),
    [Input(component_id='submit', component_property='n_clicks')],
    [State(component_id='option_in2', component_property='value')],
)   

def update_graph_3(clicks, input_value):
    input1 = "WIKI/" + input_value[0]
    data1 = quandl.get(input1)

    input2 = "WIKI/" + input_value[1]
    data2 = quandl.get(input2)

    header = dict(values=[str(input_value[0]), str(input_value[1])],
              align = ['left','center'],
              font = dict(color = 'white', size = 12),
              fill = dict(color='#119DFF')
             )
    cells = dict(values=[data1.Open.pct_change()[1:6].round(3), 
                         data2.Open.pct_change()[1:6].round(3)],
             align = ['left','center'],
             fill = dict(color=["yellow","white"])
            )
    trace = go.Table(header=header, cells=cells)
    data2 = [trace]
    figure2 = dict(data=data2)
    return figure2

#RangeSlider
@app.callback(
    Output('figure', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_years):
    filtered_df = df[
        (df.Date >= selected_years[0]) &
        (df.Date <= selected_years[1])
    ]

    trace = [go.Scatter(
        x=filtered_df.Date,
        y=filtered_df['Value'],
        mode='lines',
        fill='tonexty'
    )]

    return {
        'data': trace,
        'layout': go.Layout(
            title='<b>US GDP over time</b>',
            xaxis={'title': 'Year'},
            yaxis={'title': 'GDP Value'}
        )}

if __name__ == '__main__':
    app.run_server()
