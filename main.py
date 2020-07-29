from db import models, crud
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from db.database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI(
    title='Lusobrasilidades',
    description='Este projeto visa fornecer informações sobre localidades no Brasil e em Portugal, com dados históricos relevantes',
    version='1.0'
)
templates = Jinja2Templates(directory='templates')
models.Base.metadata.create_all(bind=engine)

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
def brasil(request: Request, estado=None, municipio=None, db:Session = Depends(get_db)):
    
    places = crud.get_local_brasil(db).all()
    
    if estado:
        places = crud.get_brasil_estado(db, estado)
        
    if municipio:
        places = crud.get_brasil_municipio(db, municipio)
        
    return templates.TemplateResponse('brasil.html', {
        'request': request,
        'places': places,
        'estado': estado,
        'municipio': municipio
    })

@app.get("/portugal")
def portugal(request: Request, distrito=None, municipio=None, freguesia=None, db:Session = Depends(get_db)):
    
    places = crud.get_local_portugal(db).all()
    
    if distrito:
        places = crud.get_portugal_distrito(db, distrito)
    
    if municipio:
        places = crud.get_portugal_municipio(db, municipio)
    
    if freguesia:
        places = crud.get_portugal_freguesia(db, freguesia)
    
    return templates.TemplateResponse('portugal.html', {
        'request': request,
        'places': places,
        'distrito': distrito,
        'municipio': municipio,
        'freguesia': freguesia
    })
