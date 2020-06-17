import threading
import json
from flask import Flask, jsonify, request, abort, make_response
from flask_restplus import Api, Resource, reqparse
from flask_restplus import Namespace
from conf import db, app
from models import Finanzas_base


"""Comenzamos API Flask"""
finanzas_base_api = Namespace('finanzas_base')


### Definimos los argumentos a recibir para crear clientes
parser_cliente = reqparse.RequestParser()
parser_cliente.add_argument('nombre', type=str, required=True)
parser_cliente.add_argument('codigo', type=str, required=True)
parser_cliente.add_argument('direccion', type=str, required=True)
parser_cliente.add_argument('contacto_nombre', type=str, required=True)
parser_cliente.add_argument('contacto_apellidos', type=str, required=True)
parser_cliente.add_argument('poblacion', type=str, required=True)
parser_cliente.add_argument('cp', type=str, required=False)
parser_cliente.add_argument('telefono_fijo', type=str, required=False)
parser_cliente.add_argument('telefono_movil', type=str, required=True)
parser_cliente.add_argument('email', type=str, required=True)

### Definimos los argumentos a recibir para eliminar clientes
parser_cliente_delete = reqparse.RequestParser()
parser_cliente_delete.add_argument('nombre', type=str, required=True)

### Definimos los argumentos a recibir para modificar clientes
parser_cliente_update = reqparse.RequestParser()
parser_cliente_update.add_argument('nombre', type=str, required=True)
parser_cliente_update.add_argument('campo', type=str, required=True)
parser_cliente_update.add_argument('nuevo_valor', type=str, required=True)



@finanzas_base_api .route('/', methods=['POST', 'GET', 'DELETE', 'PUT', 'PATCH'])
class ClienteRegistration(Resource):
    def get(self):
        """Devuelve lista total de clientes"""
        ## Recorre base de datos y lee notificaciones

        clientes = Cliente.query.all()
        results = [
            {
                "nombre": cliente.nombre,
                "codigo": cliente.codigo,
                "direccion": cliente.direccion,
                "contacto_nombre": cliente.contacto_nombre,
                "contacto_apellidos": cliente.contacto_apellidos,
                "poblacion": cliente.poblacion,
                "cp": cliente.cp,
                "telefono_fijo": cliente.telefono_fijo,
                "telefono_movil": cliente.telefono_movil,
                "email": cliente.email

            } for cliente in clientes]

        return {"Total de clientes": len(results), "Clientes": results}

    @finanzas_base_api .expect(parser_cliente, validate=True)
    def post(self):
        """Crea cliente nuevo, mira si ya estaba creado"""
        data = parser_cliente.parse_args()
        nombre = str(data.get('nombre')).lower()
        codigo = str(data.get('codigo')).lower()
        direccion = str(data.get('direccion')).lower()
        contacto_nombre = str(data.get('contacto_nombre')).lower()
        contacto_apellidos = str(data.get('contacto_apellidos')).lower()
        poblacion = str(data.get('poblacion')).lower()
        cp = str(data.get('cp')).lower()
        telefono_fijo = str(data.get('telefono_fijo')).lower()
        telefono_movil = str(data.get('telefono_movil')).lower()
        email = str(data.get('email')).lower()

        busca_nombre = Cliente.find_by_nombre(nombre)
        if type(busca_nombre) == Cliente: #Compara si existe nombre en base de datos
            return {'message': f'Cliente {nombre} already exists'}

        cliente = Cliente(
            nombre=nombre,
            codigo=codigo,
            direccion=direccion,
            contacto_nombre=contacto_nombre,
            contacto_apellidos=contacto_apellidos,
            poblacion=poblacion,
            cp=cp,
            telefono_fijo=telefono_fijo,
            telefono_movil=telefono_movil,
            email=email,

        )
        try:
            db.session.add(cliente)
            db.session.commit()

            return (
                {
                    'message': f'Cliente {nombre} fue creado con éxito'
                },
                200
            )
        except:
            return ({'message': f'Something went wrong'}, 500)

    @finanzas_base_api.expect(parser_cliente_update, validate=True)
    def put(self):
        """Actualiza cliente existente, si existe"""
        data = parser_cliente_update.parse_args()
        nombre = str(data.get('nombre')).lower()
        campo = str(data.get('campo')).lower()
        nuevo_valor = str(data.get('nuevo_valor')).lower()

        busca_nombre = Cliente.find_by_nombre(nombre)
        if type(busca_nombre) != Cliente:  # Compara si existe nombre en base de datos
            return {'message': f'Cliente {nombre} no existe'}

        try:
            db.session.query(Cliente).filter_by(nombre=nombre).update({campo: nuevo_valor})
            db.session.commit()

            return ({'message': f'Cliente «{nombre}» fue modifcado en el campo «{campo}» con el valor «{nuevo_valor}» exitosamente.'},200)
        except:
            return ({'message': f'Something went wrong'}, 500)

    @finanzas_base_api.expect(parser_cliente_delete, validate=True)
    def delete(self):
        """Elimina cliente, si existe"""
        data = parser_cliente_delete.parse_args()
        nombre = str(data.get('nombre')).lower()

        busca_nombre = Cliente.find_by_nombre(nombre)
        if type(busca_nombre) != Cliente:  # Compara si ya existe nombre en base de datos
            return {'message': f'Cliente con el nombre: {nombre} ya no existe'}

        db.engine.execute("delete from cliente where nombre = '%s'" % (nombre))
        db.session.commit()
        return ({'message': f'Cliente {nombre} was deleted'}, 200)