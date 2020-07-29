from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import ReturnTypeFromArgs
from . import models

class unaccent(ReturnTypeFromArgs):
    pass

def get_local_portugal(db: Session):
    return db.query(models.Portugal)

def get_portugal_distrito(db: Session, distrito: str):
    return db.query(models.Portugal).filter(unaccent(models.Portugal.distrito).ilike(distrito))

def get_portugal_municipio(db: Session, municipio: str):
    return db.query(models.Portugal).filter(unaccent(models.Portugal.municipio).ilike(municipio))

def get_portugal_freguesia(db: Session, freguesia: str):
    return db.query(models.Portugal).filter(unaccent(models.Portugal.freguesia).ilike(freguesia))

def get_local_brasil(db: Session):
    return db.query(models.Brasil)

def get_brasil_estado(db: Session, estado: str):
    return db.query(models.Brasil).filter(unaccent(models.Brasil.estado).ilike(estado))

def get_brasil_municipio(db: Session, municipio: str):
    return db.query(models.Brasil).filter(unaccent(models.Brasil.municipio).ilike(municipio))