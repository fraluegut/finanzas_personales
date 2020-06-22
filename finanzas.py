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
# 2. Traer todos los archivos que ya se han subido a localhost.
# 2. Abrir el archivo excel
# 3. Por cada fila de archivo excel: comprobar si ese registro existe y si no, subirlo a la base de datos.

import pandas as pd
#
# import mysql.connector
# print("Iniciando...")
# # 1. Conectarse a la base de datos en localhost
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="finanzas"
# )



# archivo = "HOla"
# mycursor = mydb.cursor()
# sql = "INSERT INTO archivos_incorporados(id, archivo) VALUES(%s)"%(archivo)
#
# mycursor.execute(sql)
# mydb.commit()

# print(len("Compra Amzn Mktp Es*go4r20ck5, 800-279-6620, Tarjeta 5163830112581329 , Comision 0,00"))
# #
# sql = "INSERT INTO finanzas(fecha_valor, fecha_operacion, concepto, importe, saldo, identificador) VALUES(%s,%s,%s,%s, %s, %s)"
# # identificador = str(valores[val][0]) + "_" + str(valores[val][1]) + "_" + str(valores[val][3])
#     print("Identificador: ")
#     print(identificador)
#
#
#
#
# valores_a_insertar = (valores[val][0], valores[val][1], valores[val][2], valores[val][3], valores[val][4], identificador)
# valores_a_insertar = (1, d(2020-01-01 00:00:00), 1, 1, 1, 1)
# #     print("Valor a insertar: ")
# #     print(valores_a_insertar)
# mycursor.execute(sql, valores_a_insertar)
# mydb.commit()
# #     print(mycursor.rowcount, "Registro insertado satisfactoriamente.")

# data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
df = pd.read_excel("Registros_CC_Agueda.xlsx")
# calling head() method
# storing in new variable
print(list(df.columns.values))
#


# # 2. Abrir todos los archivos excel dentro de una carpeta
# import glob, os
# os.chdir("/home/fraluegut/PycharmProjects/finanzas_personales/")
# archivos_agregados = []
# for file in glob.glob("*.txt"):
#     print(file)
#     if file == 'archivo_lista.txt':
#         print("El archivo archivo_lista.txt existe")
#         arch = open('archivo_lista.txt', 'r')
#         for linea in arch:
#             archivos_agregados.append(int(linea))
#         arch.close()
#     else:
#         print("El archivo archivo_lista.txt no existe")
#
#
# print("Archivos agregados A:")
# print(archivos_agregados)
#
#
#
# print("Archivos agregados B:")
# print(archivos_agregados)
#
# for file in glob.glob("*.xlsx"):
#     if file not in archivos_agregados:
#         archivos_agregados.append(file)
#         print(file)
#         print("Archivo %s agregado" %(file))
#
#
# def guardar_datos(datos):
#     with open("datos.txt", "w") as f:
#
#         f.write(str(archivos_agregados))
# def cargar_datos():
#     with open("datos.txt", "r") as f:
#         datos = [[d1, int(d2), int(d3)]
#                      for d1, d2, d3 in (l.rstrip().split(",") for l in f)]
#         print(datos)
#         return datos
#
# print("Impreso")
# f = open("datos.txt", "r")
# print(f.read())
# impreso = f.read()
#
# def Convert(string):
#     li = list(string.split(","))
#     print(li)
#     return li
#
# # impreso = eval('[' + impreso + ']')
# # print("Imprimido")
# # print(impreso)
#
# a = ','.join(impreso)
# print("A: %s" %(a))
# # Driver code
# # Convert(impreso)
# # print(Convert(impreso))
#
# datos = cargar_datos()
#
#
# nuevo_archivo = "../archivo_lista.txt"
# f = open(nuevo_archivo, 'a+')
#
# for i in archivos_agregados:
#     f.write(i)
#     #print(i)
# f.close()
#
# print("Archivos agregados C:")
# print(archivos_agregados)
# #
# archivo_banco = 'export2020612.xlsx'
# df = pd.read_excel(archivo_banco)
# print(df)
# valores = []
# for index, row in df.iterrows():
#     if index > 6:
#         print(row['Unnamed: 0'], row['Unnamed: 1'], row['CUENTA 123 SMART.'], row['FECHA'], row['Unnamed: 4'])
#         linea = [row['Unnamed: 0'], row['Unnamed: 1'], row['CUENTA 123 SMART.'], row['FECHA'], row['Unnamed: 4']]
#         print("Valor añadido: " + str(index))


#
# # Get number of rows
# index = df.index
# number_of_rows = len(index)
# print(number_of_rows)
#
#
# # Get list of columns
# columnas = list(df.columns.values)
# print(columnas)
#
# # 3. Por cada fila de archivo excel: comprobar si ese registro existe y si no, subirlo a la base de datos.
# mycursor = mydb.cursor()
# valores = []
# for index, row in df.iterrows():
#     # if row['Unnamed: 0'] > 7:
#     if index > 6:
#         # print(row['Unnamed: 0'], row['Unnamed: 1'], row['CUENTA 123 SMART.'], row['FECHA'], row['Unnamed: 4'])
#         linea = [row['Unnamed: 0'], row['Unnamed: 1'], row['CUENTA 123 SMART.'], row['FECHA'], row['Unnamed: 4']]
#         valores.append(linea)
#         # print("Valor añadido: " + str(index))
#
# print(valores)
# print("SEPARACIÓN")
# print(valores[0][0])
# print("LEN")
# print(len(valores))


# for val in range(len(valores) + 1):
#
#
#
#     print("VAL")
#     print(val)
#
#     # print([valores[val][0],valores[val][1],valores[val][2],valores[val][3],valores[val][4]])
#     sql = "INSERT INTO finanzas(fecha_valor, fecha_operacion, concepto, importe, saldo, identificador) VALUES(%s,%s,%s,%s, %s, %s)"
#     identificador = str(valores[val][0]) + "_" + str(valores[val][1]) + "_" + str(valores[val][3])
#     print("Identificador: ")
#     print(identificador)
#
#
#
#
#     valores_a_insertar = (valores[val][0], valores[val][1], valores[val][2], valores[val][3], valores[val][4], identificador)
#     print("Valor a insertar: ")
#     print(valores_a_insertar)
#     mycursor.execute(sql, valores_a_insertar)
#     mydb.commit()
#     print(mycursor.rowcount, "Registro insertado satisfactoriamente.")

# df = pd.DataFrame(valores, columns=["fecha_valor", "fecha_operacion", "concepto", "importe", "saldo", "identificador"])
# print(df)
#
# print("LISTA")
#
# # print(type(valores_a_insertar))
# lista_fechas = []
#
# lista_fechas.append(df.fecha_valor)
# print("LISTA_2")
# print(lista_fechas)
#
# ## DASH
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
#                 {'x': df.fecha_valor, 'y': df.saldo, 'type': 'bar', 'name': 'SF'},
#
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
