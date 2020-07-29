from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import ReturnTypeFromArgs
from . import models

class unaccent(ReturnTypeFromArgs):
    pass

def get_local_portugal(db: Session):
    return db.query(models.Portugal)

def get_portugal_distrito(db: Session, distrito: str):
    contains = '%{}%'.format(distrito)
    return db.query(models.Portugal).filter(unaccent(models.Portugal.distrito).ilike(contains))

def get_portugal_municipio(db: Session, municipio: str):
    contains = '%{}%'.format(municipio)
    return db.query(models.Portugal).filter(unaccent(models.Portugal.municipio).ilike(contains))

def get_portugal_freguesia(db: Session, freguesia: str):
    contains = '%{}%'.format(freguesia)
    return db.query(models.Portugal).filter(unaccent(models.Portugal.freguesia).ilike(contains))

def get_local_brasil(db: Session):
    return db.query(models.Brasil)

def get_brasil_estado(db: Session, estado: str):
    contains = '%{}%'.format(estado)
    return db.query(models.Brasil).filter(unaccent(models.Brasil.estado).ilike(contains))

def get_brasil_municipio(db: Session, municipio: str):
    contains = '%{}%'.format(municipio)
    return db.query(models.Brasil).filter(unaccent(models.Brasil.municipio).ilike(contains))