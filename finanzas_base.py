import threading
import json
from flask import Flask, jsonify, request, abort, make_response
from flask_restplus import Api, Resource, reqparse
from flask_restplus import Namespace
from conf import db, app
from models import Registros_bancarios

import pandas as pd
import numpy as np
from ast import literal_eval
from functools import wraps

"""Comenzamos API Flask"""
finanzas_base_api = Namespace('finanzas_base')


def errorhandler(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            try:
                db.close()
                return f(*args, **kwargs)
            except Exception as ex:
                return {'msg': {'exception': str(ex)}},500

    return wrapper

@finanzas_base_api .route('/', methods=['POST', 'GET', 'DELETE', 'PUT', 'PATCH'])
class FinanzasBase(Resource):
    def get(self):
        """Devuelve lista total de finanzas"""
        ## Recorre base de datos y lee notificaciones

        finanzas_bases = Registros_bancarios.query.all()
        results = [
            {
                "Id": finanzas_base.id,
                "Fecha_valor": str(finanzas_base.fecha_valor),
                "Fecha_operacion": str(finanzas_base.fecha_operacion),
                "Concepto": finanzas_base.concepto,
                "Importe": finanzas_base.importe,
                "Saldo": finanzas_base.saldo,
                "Identificador": finanzas_base.identificador,
                "Tarjeta de": finanzas_base.tarjeta_de,
            } for finanzas_base in finanzas_bases]

        return {"Total de registros en finanzas_base": len(results), "Finanzas base": results}
