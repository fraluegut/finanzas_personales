"""
API FLASK
Importamos librerias
"""

import threading
import json
from flask import Flask, jsonify, request, abort, make_response
from flask_restplus import Api
from conf import app
import request

## Importamos los namespace
from finanzas_base import finanzas_base_api


"""Comenzamos API Flask para interactuar con produccion"""
api = Api(app=app)
ns_api = api.namespace('api_v1', description='Api HRM')

## Añadimos los namespaces
api.add_namespace(finanzas_base_api)


if __name__ == '__main__':
    ## Corre api
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)

