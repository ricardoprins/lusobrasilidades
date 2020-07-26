from sqlalchemy.orm import Session
import models, schemas

def get_local_portugal(db: Session):
    return db.query(models.Portugal)

def get_portugal_distrito(db: Session, distrito: str):
    return db.query(models.Portugal).filter(models.Portugal.distrito.ilike(distrito))

def get_portugal_municipio(db: Session, municipio: str):
    return db.query(models.Portugal).filter(models.Portugal.municipio.ilike(municipio))

def get_portugal_freguesia(db: Session, freguesia: str):
    return db.query(models.Portugal).filter(models.Portugal.freguesia.ilike(freguesia))