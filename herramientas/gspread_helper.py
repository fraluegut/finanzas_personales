import gspread
from gspread_dataframe import set_with_dataframe, get_as_dataframe
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


def get_credencial_gspread(FILE_GOOGLE_GSPREAD=None):
    """
    Carga credenciales desde archivo
    :param FILE_GOOGLE_GSPREAD:
    :return:
    """
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(FILE_GOOGLE_GSPREAD,
                                                                   scope)
    return credentials

# 22627501198-c9kka32f1b76h6ehfj5kcp9rttc4c7r7.apps.googleusercontent.com
# 3z33bgQJorldUbRlLN75Wb2w
class Gspread_Tools(object):
    """
    Herramientas para manejo de google sheets
    """

    def __init__(self, file_credencials=None):
        self.gc = None
        self.credentials = get_credencial_gspread(FILE_GOOGLE_GSPREAD=file_credencials)
        self.open_spreads = {}

    def connect(self):
        """
        :return:
        """
        self.gc = gspread.authorize(self.credentials)
        self.open_spreads = {}

    def _check_spread(self, spread_name=None):
        if spread_name not in self.open_spreads:  # miramos si esta
            self.open_spreads[spread_name] = self.gc.open(spread_name)

    def get_as_dataframe(self,spread_name,sheet_name):
        self._check_spread(spread_name=spread_name)
        wks = self.open_spreads[spread_name].worksheet(sheet_name)
        frame = get_as_dataframe(wks)
        return  frame[[c for c in frame.columns if 'Unnamed' not in c ]]

    def get_serie(self, spread_name=None, sheet_name=None,
                  col_str=['account_id'], date_index=True):
        """
        Lee hoja que tiene como primera columna date_time
        :param sheet_name:
        :return:
        """
        self._check_spread(spread_name=spread_name)
        wks = self.open_spreads[spread_name].worksheet(sheet_name)
        _frame = get_as_dataframe(wks, include_index=True, index_col=0)
        if date_index:
            _frame.index = pd.to_datetime(_frame.index)  # pasamos a date_time
            _frame.index.name = 'date_time'  # por defecto
            _frame = _frame[
                _frame.index <= _frame.index.max()]  ## filtro de nan en indices
        try:
            col_filtro = [c for c in _frame.columns if 'Unnamed' not in c]
            _frame = _frame[col_filtro]  # filtro de lectura de Unnamed
        except:
            pass
        _frame.columns = [str(c).split('.')[0] for c in _frame.columns]  # nombre columnas  siemre str

        col = _frame.columns.tolist()
        if len(col_str) > 0:  ## columnas que son str y pueden venir en float con punto
            for c in col_str:
                if c in col:
                    _frame[c] = [str(c).split('.')[0] for c in _frame[c].values]

        return _frame

    def get_sheet_with_formulas(self, spread_name=None, sheet_name=None, col_str=['account_id']):
        """
        Lee hoja que tiene como primera columna date_time
        :param sheet_name:
        :return:
        """

        self._check_spread(spread_name=spread_name)
        wks = self.open_spreads[spread_name].worksheet(sheet_name)
        list_of_lists = wks.get_all_values()
        _f_info = {}

        for col_n, name_col in enumerate(list_of_lists[0]):
            _f_info[name_col] = []
            for list in list_of_lists[1:]:
                dat = list[col_n]
                try:
                    dat = float(dat.replace(',', ''))
                except:
                    if len(dat) == 1 and dat == '-':
                        dat = None
                _f_info[name_col].append(dat)

        _frame_info = pd.DataFrame(_f_info)
        col = [c for c in _frame_info.columns]
        if len(col_str) > 0:  ## columnas que son str y pueden venir en float con punto
            for c in col_str:
                if c in col:
                    _frame_info[c] = [str(c).split('.')[0] for c in _frame_info[c].values]

        return _frame_info

    def save_frame(self, frame, spread_name=None, sheet_name=None, clear=True, include_index=True):
        """
        Guarda dataframe
        :param frame:
        :param spread_name:
        :param sheet_name:
        :param clear:  Borra hoja antes de grabar
        :return:
        """
        self._check_spread(spread_name=spread_name)
        wks = self.open_spreads[spread_name].worksheet(sheet_name)
        if clear:
            wks.clear()  # borrar contenido

        set_with_dataframe(wks, frame, include_index=include_index)

    def sheet_from_dict(self, spread_name=None, sheet_dict=None,
                        clear=True, include_index=True):
        """
        Guarda varios  dataframes desde un diccionario
        :param spread_name: Nombre de la hoja
        :param sheet_dict: diccionario nombres de sheet como claves,
        dataframes como values
        :param clear:  Borra hoja antes de grabar
        :return:
        """
        print('B')
        self._check_spread(spread_name=spread_name)
        print('A', sheet_dict.keys())
        for sheet_name, sheet_frame in sheet_dict.items():
            wks = self.open_spreads[spread_name].worksheet(sheet_name)
            if clear:
                wks.clear()  # borrar contenido
            set_with_dataframe(wks, sheet_frame,
                               include_index=include_index)
        return
