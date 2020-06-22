import datetime as dt
import pandas as pd
import os
import xlrd
import glob, os

from models import db, Registros_bancarios

path = os.path.abspath(__file__)
path_modulo = os.path.dirname(path)  # direccion del modulo




##########################################################
################## TABLAS NUEVAS #########################
##########################################################

def main(DATABASE_TYPE='sqlite_local'):
    ### Tablas auxiliares ####

    rellenar_registros_tarjeta_javier = True
    rellenar_registros_tarjeta_agueda = True

    os.environ['DATABASE_TYPE'] = DATABASE_TYPE
    from models import db, Registros_bancarios
    from conf import engine

    ### Tablas auxiliares ####
    # Registros_bancarios.__table__.create(engine)

    ##### TABLAS PARA RELLENAR ####

    archivos_agregados = []
    if rellenar_registros_tarjeta_agueda:
        df = pd.read_excel("Registros_CC_Agueda.xlsx")
        for index, row in df.iterrows():
            if index > 7:
                registros_bancarios_ = Registros_bancarios()
                registros_bancarios_.fecha_operacion = row['Unnamed: 0']
                registros_bancarios_.fecha_valor = row['Unnamed: 1']
                registros_bancarios_.concepto = row['CUENTA 123 SMART.']
                registros_bancarios_.importe = row['Unnamed: 3']
                registros_bancarios_.saldo = row['Unnamed: 4']
                registros_bancarios_.identificador = str(row['Unnamed: 0']) + "_" + str(row['Unnamed: 1'])+"_"+ str(row['Unnamed: 3'])+"_"+str("Agueda")
                registros_bancarios_.tarjeta_de = "Águeda Sánchez"
                db.add(registros_bancarios_)
        db.commit()



    if rellenar_registros_tarjeta_javier:
        df = pd.read_excel("Registros_CC_Javier.xlsx")
        for index, row in df.iterrows():
            if index > 7:
                registros_bancarios_ = Registros_bancarios()
                registros_bancarios_.fecha_operacion = row['Unnamed: 0']
                registros_bancarios_.fecha_valor = row['Unnamed: 1']
                registros_bancarios_.concepto = row['CUENTA 123 SMART.']
                registros_bancarios_.importe = row['Unnamed: 3']
                registros_bancarios_.saldo = row['Unnamed: 4']
                registros_bancarios_.identificador = str(row['Unnamed: 0']) + "_" + str(row['Unnamed: 1'])+"_"+ str(row['Unnamed: 3'])+"_"+str("Javier")
                registros_bancarios_.tarjeta_de = "Javier Luengo"

                db.add(registros_bancarios_)
            db.commit()


if __name__ == '__main__':
    main(DATABASE_TYPE='mariadb_nube')
