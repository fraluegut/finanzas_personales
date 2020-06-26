

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

import plotly.express as px
from models import Registros_bancarios
import plotly.graph_objects as go

finanzas_bases = Registros_bancarios.query.all()
results = [{    "Id": finanzas_base.id,
                "Fecha_valor": str(finanzas_base.fecha_valor),
                "Fecha_operacion": str(finanzas_base.fecha_operacion),
                "Concepto": finanzas_base.concepto,
                "Importe": finanzas_base.importe,
                "Saldo": finanzas_base.saldo,
                "Identificador": finanzas_base.identificador,
                "Tarjeta de": finanzas_base.tarjeta_de,
            } for finanzas_base in finanzas_bases]

print(results)

fechas = []
for fecha in range(len(results)):
    fechas.append(results[fecha]["Fecha_operacion"])

importes = []
for importe in range(len(results)):
    importes.append(results[importe]["Importe"])

print(fechas)
print(len(fechas))
print(importes)
print(len(importes))

d = {'fechas': fechas, 'importes': importes}
df = pd.DataFrame(data=d)
print(df)

fechas_unicas = list(set(fechas))
print(fechas_unicas)

print(len(fechas))
print(len(fechas_unicas))


df = pd.DataFrame({'Date': fechas,
                   'Importe': importes})
print("FORMULANDO: ")
def get_count(values):
    return len(values)
importes= df.groupby(['Date'])['Importe'].agg('sum')
print("DF")

print(importes)

print("importes")
print(importes[0])
df['Fecha'] = df.index
d = {'fechas': importes['Date'], 'importes': importes['Importe']}
df = pd.DataFrame(data=d)
print("Nuevo")
print(df)
# print(df.groupby(by=['Importe','Date']).sum().groupby(level=[0]).cumsum())

# print(df.groupby(['Date'])['Importe'].series.agg(get_count))

# importe_por_dia = []
# for dia in fechas:
#
#     for day in range(len(fechas_unicas)):
#         suma = df['importes'][day]
#
#         print(suma)
#         importe_por_dia.append(suma)
#     total = {"dia":dia, "dinero":sum(importe_por_dia)}

# importe_total_por_fechas_unicas = {'fechas': fechas_unicas, 'importes': importe_por_dia}
# df = pd.DataFrame(data=importe_total_por_fechas_unicas)
# print("Df final: ")
# print(df)
# ## DASH
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# app.layout = html.Div(children=[
#     html.H1(children='Finanzas personales'),
#
#     html.Div(children='''
#         Visor de gastos e ingresos acumulados por día
#     '''),
#
#     dcc.Graph(
#         id='Visor de gastos e ingresos acumulados por día',
#         figure=px.scatter(x=df['fechas'], y=df['importes']),
#
#
#     ),
#     dcc.Graph(
#         id='example-graph',
#         figure=px.scatter(x=df['fechas'], y=df['importes']),
#
#     ),
# ])
#
# if __name__ == '__main__':
#     app.run_server(debug=True)
