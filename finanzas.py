# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pymysql



class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost', # ip
            user='root',
            password='',
            db='finanzas'
        )

        self.cursor = self.connection.cursor()

        print("Conexión establecida exitosamente")

    def select_user(self):

        sql = 'SELECT * FROM users'
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            print("Id:", user[0])
            print("Username:", user[1])
            print("Email:", user[2])
        except Exception as e:
            raise

database = DataBase()
database.select_user()


#
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# app.layout = html.Div(children=[
#     html.H1(children='Finanzas personales'),
#
#     html.Div(children='''
#         Visor de economía intrafamiliar
#     '''),
#
#     dcc.Graph(
#         id='example-graph',
#         figure={
#             'data': [
#                 {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
#                 {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
#             ],
#             'layout': {
#                 'title': 'Dash Data Visualization'
#             }
#         }
#     )
# ])
#
# if __name__ == '__main__':
#     app.run_server(debug=True)