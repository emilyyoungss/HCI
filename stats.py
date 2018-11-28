import plotly.plotly as py
import plotly.graph_objs as go

data = [go.Bar(
            x=['user', 'recommended', 'average'],
            y=[7.9, 3.3, 5.9]
    )],
layout = go.Layout(
    title='Consumption of alcohol per unit'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='units')


caloriesData = [go.Bar(
        x=['user', 'recommended', 'average'],
        y=[581, 243, 459]
)],

caloriesLayout = go.Layout(
    title = 'Calorie counter from alcohol consumption'
    
)
figure = go.Figure(data=caloriesData, layout=caloriesLayout)
py.iplot(figure, filename='calories')
