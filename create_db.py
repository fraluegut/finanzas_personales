import datetime as dt
import pandas as pd
import os

path = os.path.abspath(__file__)
path_modulo = os.path.dirname(path)  # direccion del modulo

##########################################################
################## TABLAS NUEVAS #########################
##########################################################

def main(DATABASE_TYPE='sqlite_local'):
    ### Tablas auxiliares ####
    _hacer_estados = False


    os.environ['DATABASE_TYPE'] = DATABASE_TYPE
    from models import db, Finanzas
    from conf import engine
    import conf
    # Create the database

    # file = conf.file_conf_google
    # gspread = gspread_helper.Gspread_Tools(file_credencials=file)
    # gspread.connect()

    ### Tablas auxiliares ####
    Finanzas.__table__.create(engine)

    ##### TABLAS AUXILIARES ####

    # if _hacer_turnos:
    #     df = gspread.get_sheet_with_formulas('BBDD provisional SIES', 'Turnos')
    #     df = df[df['id'] != '']
    #     for row in df.iterrows():
    #         Turnos_ = Turnos()
    #         Turnos_.id = row[1].to_dict()['id']
    #         Turnos_.nombre_turno = row[1].to_dict()['nombre_turno']
    #
    #         db.add(Turnos_)
    #     db.commit()




if __name__ == '__main__':
    main(DATABASE_TYPE='mariadb_nube')
