import os
from models import db, engine

import datetime as dt
# Data to initialize database with
PEOPLE = [
    {'alias': 'pepe', 'pin': '0987', 'cargo_id': '1'},
    {'alias': 'antonio', 'pin': '1111', 'cargo_id': '2'},
    {'alias': 'jose', 'pin': '2222', 'cargo_id': '3'}
]

CLIENTES = [
    {'nombre': 'endesa',
     'codigo': '123214',
     'direccion': 'calle paloma 12',
     'contacto_nombre': 'fernando',
     'contacto_apellidos': 'gonzalez jimenez',
     'poblacion': 'tomares',
     'cp': '41940',
     'telefono_fijo': '954121212',
     'telefono_movil': '654654654',
     'email': 'jose@gmail.com'}
]


