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

# 1. Conectarse a la base de datos en localhost
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="finanzas"
)

# 2. Abrir el archivo excel
archivo_banco = 'export2020612.xlsx'
df = pd.read_excel(archivo_banco)
# print(df)

# Get number of rows
index = df.index
number_of_rows = len(index)
# print(number_of_rows)


# Get list of columns
columnas = list(df.columns.values)
# print(columnas)

# 3. Por cada fila de archivo excel: comprobar si ese registro existe y si no, subirlo a la base de datos.
mycursor = mydb.cursor()
valores = []
for index, row in df.iterrows():
    # if row['Unnamed: 0'] > 7:
    if index > 6:
        # print(row['Unnamed: 0'], row['Unnamed: 1'], row['CUENTA 123 SMART.'], row['FECHA'], row['Unnamed: 4'])
        linea = [row['Unnamed: 0'], row['Unnamed: 1'], row['CUENTA 123 SMART.'], row['FECHA'], row['Unnamed: 4']]
        valores.append(linea)
        # print("Valor añadido: " + str(index))

# print(valores)
# print("SEPARACIÓN")
# print(valores[0][0])
# print("LEN")
# print(len(valores))
for val in range(len(valores) + 1):
    print("VAL")
    print(val)

    # print([valores[val][0],valores[val][1],valores[val][2],valores[val][3],valores[val][4]])
    sql = "INSERT INTO finanzas(fecha_valor, fecha_operacion, concepto, importe, saldo, identificador) VALUES(%s,%s,%s,%s, %s, %s)"
    identificador = str(valores[val][0]) + "_" + str(valores[val][1]) + "_" + str(valores[val][3])
    print("Identificador: ")
    print(identificador)




    valores_a_insertar = (valores[val][0], valores[val][1], valores[val][2], valores[val][3], valores[val][4], identificador)
    print("Valor a insertar: ")
    print(valores_a_insertar)
    mycursor.execute(sql, valores_a_insertar)
    mydb.commit()
    print(mycursor.rowcount, "Registro insertado satisfactoriamente.")

df = pd.DataFrame(valores, columns=["fecha_valor", "fecha_operacion", "concepto", "importe", "saldo", "identificador"])
print(df)

print("LISTA")

print(type(valores_a_insertar))
lista_fechas = []

lista_fechas.append(df.fecha_valor)
print("LISTA_2")
print(lista_fechas)

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
                {'x': df.fecha_valor, 'y': df.saldo, 'type': 'bar', 'name': 'SF'},

            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
