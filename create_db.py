import datetime as dt
import pandas as pd
import os

path = os.path.abspath(__file__)
path_modulo = os.path.dirname(path)  # direccion del modulo


from herramientas import gspread_helper
import conf
    # Create the database

#
# file = conf.file_conf_google
# gspread = gspread_helper.Gspread_Tools(file_credencials=file)
# gspread.connect()

##########################################################
################## TABLAS NUEVAS #########################
##########################################################

def main(DATABASE_TYPE='sqlite_local'):
    ### Tablas auxiliares ####
    rellenar_finanzas_google = False
    rellenar_finanzas = True


    os.environ['DATABASE_TYPE'] = DATABASE_TYPE
    from models import db, Registros_bancarios
    from conf import engine
    import conf
    # Create the database

    # file = conf.file_conf_google
    # gspread = gspread_helper.Gspread_Tools(file_credencials=file)
    # gspread.connect()

    ### Tablas auxiliares ####
    Registros_bancarios.__table__.create(engine)

    ##### TABLAS PARA RELLENAR ####

    if rellenar_finanzas_google:
        df = gspread.get_sheet_with_formulas('Finanzas personales', 'Registros bancarios')
        df = df[df['id'] != '']
        for row in df.iterrows():
            Registros_bancarios = Registros_bancarios()
            Registros_bancarios.id = row[1].to_dict()['id']
            Registros_bancarios.fecha_operacion = row[1].to_dict()['fecha operacion']
            Registros_bancarios.fecha_valor = row[1].to_dict()['fecha valor']
            Registros_bancarios.concepto = row[1].to_dict()['concepto']
            Registros_bancarios.importe = row[1].to_dict()['importe']
            Registros_bancarios.saldo = row[1].to_dict()['saldo']
            Registros_bancarios.tarjeta_de = row[1].to_dict()['tarjeta de']


            db.add(Registros_bancarios)
        db.commit()
    if rellenar_finanzas:
        archivo_banco = 'export2020612.xlsx'
        df = pd.read_excel(archivo_banco)

        for index, row in df.iterrows():
            if index > 6:
                print(row['Unnamed: 0'], row['Unnamed: 1'], row['CUENTA 123 SMART.'], row['FECHA'], row['Unnamed: 4'])
                linea = [row['Unnamed: 0'], row['Unnamed: 1'], row['CUENTA 123 SMART.'], row['FECHA'],
                         row['Unnamed: 4']]
                print("Valor añadido: " + str(index))

                Registros_bancarios_ = Registros_bancarios()
                Registros_bancarios_.fecha_operacion = row['Unnamed: 0']
                Registros_bancarios_.fecha_valor = row['Unnamed: 1']
                Registros_bancarios_.concepto = row['CUENTA 123 SMART.']
                Registros_bancarios_.importe = row['FECHA']
                Registros_bancarios_.saldo = row['Unnamed: 4']
                Registros_bancarios_.identificador = str(row['Unnamed: 0']) + "_" + str(row['Unnamed: 1'])+"_"+ str(row['FECHA'])
                db.add(Registros_bancarios_)
        db.commit()



if __name__ == '__main__':
    main(DATABASE_TYPE='mariadb_nube')
