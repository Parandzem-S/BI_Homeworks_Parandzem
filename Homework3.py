import dash
import dash_core_components as dcc
import dash_html_components as html

import plots


app=dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})


app.layout = html.Div([

#row1
html.Div([
			html.H1(children="Homework 3,Parandzem", style={'color': '#5e0019', 'fontSize': 48, 'textAlign': 'center','fontFamily':'Comic Sans MS'}),
				],className="row"),


#row 2
html.Div([
			#First 2 columns
			html.Div([
				html.P(children="Homework 3 assumes the development of this web application using Dash and Plotly in Python. You are required to develop 6 plots (including one table) with the given layout. Subtle differences related to styling (colors etc) are allowed, yet the general layout must be kept to perceive same information as this website does. Quandl is used as a data source for 4 plots among 6, while the other 2 are based on user provided data. Some of the Quandl based plots require minor analysis using pandas. You are encouraged to follow below mentioned steps to complete the HW:"),
				html.Ol([html.Li(children="Start from first developing the 6 plots in Jupyter Notebook,"),
						html.Li(children='Once plots are ready post them into the Dash app,'),
						html.Li(children='Add HTML components (website heading etc.),'),
						html.Li(children='Structure the layout of the dashboard.')]),
			], className='four columns'),

			#Second 2 columns
			html.Div([
				html.H6(children="Graph1", style={'textAlign': 'left', 'fontWeight':'bold'}),
				html.P(children="The graph on the right hand side is showing correlations of different variables (call them from x1 to x8) with employee churn. Data is artificial, manually inputted by the developer. Recreate the graph. Small coloring or corelation value differences will be neglected."),
				], className='three columns'),
			#Third 6 columns
			html.Div([
				dcc.Graph(id='figure1', figure=plots.figure1),
				], className='five columns'),
	], className='row'),


#row 3
html.Div([
	
	html.Div([
				html.H6(children="Graph2", style={'textAlign': 'left','fontWeight':'bold'}),
				html.P(children='One the right hand side we have US GDP graphed over time. The data is sourced from QUANDL API (FRED/GDP). Your task is to recreate exactly the same graph.')
		], className="four columns"),


	html.Div([
				dcc.Graph(id='figure2', figure=plots.figure2),
				], className='eight columns'),
		],className='row'),

#row4
html.Div([
		html.Div([
				html.H6(children="Graph 3 and 4", style={'textAlign': 'left','fontWeight':'bold'}),
				html.P(children="The two graphs on this row are based on Google's stock (WIKI/GOOGL) and Bitcoin's (BCHARTS/ABUCOINSUSD) prices sourced from Quandl. First, percentage changes are calculated. Then the latter is plotted using Box plot to find the distribution and outliers. In the end the first 4 percentage changes (apart from the very first one, which is N/A) are plotted in a table. Recreate similar graphs with the same values (minor styling is neglected)."),	
			],className='three columns'),
		
		html.Div([
				dcc.Graph(id='figure3', figure=plots.figure3),
			],className="six columns"),


		html.Div([
				dcc.Graph(id='figure4', figure=plots.figure4),
			],className="three columns"),
],className='row'),


#row5
html.Div([
		html.Div([
				html.H6(children="Graph 5", style={'textAlign': 'left','fontWeight':'bold'}),
				html.P(children="Last graph is based on manually inputted data. It shows the Roadmap developed by an artificial startup. Task 1 is assumed to take the whole Janduary, while Task 2 is starting from March and ending in mid April. Afterwards, Task 3 begins and ends in the end of September. Recreate a similar Roadmap"),	
			],className='three columns'),

		html.Div([
					dcc.Graph(id='figure5', figure=plots.figure5),
					],className='eight columns'),
], className='row')

])


if __name__ == '__main__':
    app.run_server(debug=True)
