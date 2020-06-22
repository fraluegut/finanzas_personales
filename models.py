from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float,BOOLEAN
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import sqlalchemy
from conf import db, url
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import relationship

Base = declarative_base()
engine = sqlalchemy.create_engine(url)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base.query = db_session.query_property()
################## FINANZAS_BASE #########################
class Registros_bancarios(Base):
    __tablename__ = 'registros_bancarios'

    id = Column(Integer, primary_key=True)
    fecha_creacion_registro = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    tipo_registro = Column(String(32), default="nuevo", index=True, nullable=False)

    fecha_valor = Column(DateTime, index=True, nullable=False)
    fecha_operacion = Column(DateTime, index=True, nullable=False)
    concepto = Column(String(120), index=True, nullable=False)
    importe = Column(Float, index=True, nullable=False)
    saldo = Column(Float, index=True, nullable=True)
    tarjeta_de = Column(String(60), index=True, nullable=False)
    identificador = Column(String(60), index=True, nullable=False, unique=True)


    #Relaciones
    # relacion_con_nada = relationship("ID", cascade="all, delete", passive_deletes=True)


    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def __repr__(self):
        return '{}'.format(self.id)