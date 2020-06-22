import dash
import dash_core_components as dcc
import dash_html_components as html


## DASH
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Finanzas personales'),

    html.Div(children='''
        Visor de economía intrafamiliar
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': 2, 'y': 3, 'type': 'bar', 'name': 'SF'},

            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
