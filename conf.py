import os

import marshmallow as marshmallow
import connexion
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os
from flask import Flask
from flask_cors import CORS
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker



basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
app = Flask(__name__)

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
# Configure the SQLAlchemy part of the app instance

app.config['SQLALCHEMY_POOL_RECYCLE'] = 299
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 20
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3305/sistema_financiero'
url = app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3305/sistema_financiero'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Create the SQLAlchemy db instance
Base = declarative_base()
engine = sqlalchemy.create_engine(url)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base.query = db_session.query_property()

db = db_session()

_path = os.path.abspath(__file__)
_path_modulo = os.path.dirname(_path)  # direccion del modulo

