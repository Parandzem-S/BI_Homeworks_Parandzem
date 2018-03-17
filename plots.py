from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd
import plotly.figure_factory as ff
import quandl


#Graph 1-Correlations
x_values_1=[55,20,15,38]
x_values_2=[-60,-45,-20,-5]
y_values_1=['x1','x2','x3','x4']
y_values_2=['x5','x6','x7','x8']

trace_1 = go.Bar(x=x_values_1, y=y_values_1, name="Positive",orientation = 'h')
trace_2 = go.Bar(x=x_values_2, y=y_values_2, name="Negative",orientation = 'h')

layout = dict(title="<b>Correlations with employees probability of churn</b>", xaxis={"title":'values'},
		              yaxis={"title":'Variables'},barmode = 'bar')


data = [trace_1,trace_2]
figure1 = dict(data=data,layout=layout)


#Graph 2-Time Series
Data=quandl.get("FRED/GDP", authtoken="")


x_values = pd.to_datetime(Data.index.values)
y_values = Data.Value
trace = go.Scatter(x=x_values,y=y_values,mode="lines",fill= "tozeroy")

layout = dict(title="US GDP over time")
		              
data = [trace]
figure2 = dict(data=data, layout=layout)

		
#Graph3-Box Plot
Data2=quandl.get(["WIKI/GOOGL", "BCHARTS/ABUCOINSUSD"],authtoken="")

Data2=Data2.rename(columns={'WIKI/GOOGL - Open':'OpenGoogle'})
Data2=Data2.rename(columns={'BCHARTS/ABUCOINSUSD - Open':'OpenBitcoin'})

trace1 = go.Box(x=Data2.OpenBitcoin.pct_change(),name="Bitcoin")
trace2 = go.Box(x=Data2.OpenGoogle.pct_change(),name="Google")


layout = dict(title="Distribution of Price Changes")

data = [trace1,trace2]
figure3 = dict(data=data, layout=layout)


#Graph 4-Table
DataB=quandl.get(["BCHARTS/ABUCOINSUSD"],authtoken="")
DataG=quandl.get(["WIKI/GOOGL"],authtoken="4znMPd7_HKFqDvStTZ7e")

DataG=DataG.rename(columns={'WIKI/GOOGL - Open':'OpGoogle'})
DataB=DataB.rename(columns={'BCHARTS/ABUCOINSUSD - Open':'OpBitcoin'})

GooglePercent=DataG.OpGoogle.pct_change()
BitcoinPercent=DataB.OpBitcoin.pct_change()


header = dict(values=['Google','Bitcoin'],
	              align = ['left','center'],
	              font = dict(color = 'white', size = 12),
	              fill = dict(color='#119DFF')
	             )
cells = dict(values=[GooglePercent[1:5].round(3),
	                     BitcoinPercent[1:5].round(3)],
	             align = ['left','center'],
	             fill = dict(color=["yellow","white"])
	            )
trace = go.Table(header=header, cells=cells)

data = [trace]
layout = dict(width=500, height=300)
figure4 = dict(data=data, layout=layout)


#Graph 5-Startup Roadmap
df = [dict(Task="Task 1", Start='2018-01-01', Finish='2018-01-31', Resource='Idea Validation'),
	      dict(Task="Task 2", Start='2018-03-01', Finish='2018-04-15', Resource='Prototyping'),
	      dict(Task="Task 3", Start='2018-04-15', Finish='2018-09-30', Resource='Team formation')]

colors =[ '#e53509', '#6d1951','#27632f']
	              
	              
figure5 = ff.create_gantt(df,title="Sturtup Roadmap", index_col='Resource',show_colorbar=True,colors=colors)
	

		
