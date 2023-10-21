import dash
from dash import dcc
from dash import html
import plotly.graph_objects as graph

app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H2(children='Hello'),
    dcc.Graph(
        figure=graph.Figure(
            [
                graph.Bar(
                    x=['P1','P2','P3'],
                    y=[36,30,10],
                    name='wykres'
                )
            ]
        )
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
