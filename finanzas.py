# Librerías
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pymysql
import pandas as pd
import numpy as np
import xlrd

# 1. Conectarse a la base de datos en localhost
# 2. Abrir el archivo excel
# 3. Por cada fila de archivo excel: comprobar si ese registro existe y si no, subirlo a la base de datos.

import pandas as pd

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="finanzas"
)

mycursor = mydb.cursor()

sql = "INSERT INTO finanzas_personales(fecha_valor, fecha_operacion, importe, saldo) VALUES(%s,%s,%s,%s)"
val = ("2020-06-02", "2020-06-02", "1", "1")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

#
# ## DATABASE LOCALHOST
# class DataBase:
#     def __init__(self):
#         self.connection = pymysql.connect(
#             host='localhost', # ip
#             user='root',
#             password='',
#             db='finanzas'
#         )
#
#         self.cursor = self.connection.cursor()
#
#         print("Conexión establecida exitosamente")
#
#
#
# archivo_banco = 'export2020612.xlsx'
# df = pd.read_excel(archivo_banco)
# print(df)
#
# index = df.index
# number_of_rows = len(index)
#
# print(number_of_rows)
#
#
# # Get list of columns
# columnas = list(df.columns.values)
# print(columnas)
#
# def insert_datos(self):
#
#         sql = "INSERT INTO finanzas_personales(id, fecha_valor, fecha_operacion, importe, saldo) " \
#             "VALUES(%s,%s,%s,%s,%s)"
#         try:
#             self.cursor.execute(sql)
#             user = self.cursor.fetchone()
#
#             print("Id:", user[0])
#             print("Username:", user[1])
#             print("Email:", user[2])
#         except Exception as e:
#             raise
#
# database = DataBase()
# insert_datos()
#
# for index, row in df.iterrows():
#     # if row['Unnamed: 0'] > 7:
#     if index > 6:
#         print(row['Unnamed: 0'], row['Unnamed: 1'], row['CUENTA 123 SMART.'], row['FECHA'], row['Unnamed: 4'])
#         database = DataBase()
#         cursor = self.connection.cursor()
#         self.cursor.execute(sql)
#     else:
#         print(index)
#         print("Valor no incluido")
#
#
# def insert_books(books):
#     query = "INSERT INTO finanzas_personales(id, fecha_valor, fecha_operacion, importe, saldo) " \
#             "VALUES(%s,%s,%s,%s,%s)"
#
#     try:
#         db_config = read_db_config()
#         conn = MySQLConnection(**db_config)
#
#         cursor = conn.cursor()
#         cursor.executemany(query, books)
#
#         conn.commit()
#
#
#     finally:
#         cursor.close()
#         conn.close()
#
# # for row in df:
# #     if df[0] > 7:
# #         print(df[0], df[1])
# #     else:
# #         print("No")
# # ## DATABASE LOCALHOST
# # class DataBase:
# #     def __init__(self):
# #         self.connection = pymysql.connect(
# #             host='localhost', # ip
# #             user='root',
# #             password='',
# #             db='finanzas'
# #         )
# #
# #         self.cursor = self.connection.cursor()
# #
# #         print("Conexión establecida exitosamente")
# #
# #     def select_user(self):
# #
# #         sql = 'SELECT * FROM users'
# #         try:
# #             self.cursor.execute(sql)
# #             user = self.cursor.fetchone()
# #
# #             print("Id:", user[0])
# #             print("Username:", user[1])
# #             print("Email:", user[2])
# #         except Exception as e:
# #             raise
# #
# # database = DataBase()
# # database.select_user()
#
#
# ### DASH
# # external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# #
# # app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# #
# # app.layout = html.Div(children=[
# #     html.H1(children='Finanzas personales'),
# #
# #     html.Div(children='''
# #         Visor de economía intrafamiliar
# #     '''),
# #
# #     dcc.Graph(
# #         id='example-graph',
# #         figure={
# #             'data': [
# #                 {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
# #                 {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
# #             ],
# #             'layout': {
# #                 'title': 'Dash Data Visualization'
# #             }
# #         }
# #     )
# # ])
# #
# # if __name__ == '__main__':
# #     app.run_server(debug=True)