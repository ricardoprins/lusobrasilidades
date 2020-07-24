import models

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import Optional
from pydantic import BaseModel
from models import Portugal, Brasil


app = FastAPI()
templates = Jinja2Templates(directory='templates')
models.Base.metadata.create_all(bind=engine)

class LocalitySearch(BaseModel):
    locality_name: str

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse('home.html', {
        'request': request
    })

@app.get("/brasil")
def brasil(request: Request):
    return templates.TemplateResponse('brasil.html', {
        'request': request
    })

@app.get("/portugal")
def brasil(request: Request):
    return templates.TemplateResponse('portugal.html', {
        'request': request
    })

@app.post("/filter")
def filter(locality_search: LocalitySearch):
    """
    To be added later, I am tired today.
    This will filter localities' data and mess with the tables.
    """
    pass

""" def fetch_locality_data(id: int):
    db = SessionLocal()
    loc = db.query(Locality).filter(Locality.id == id).first()
"""

