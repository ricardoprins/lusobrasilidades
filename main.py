import models, schemas, crud
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from models import Portugal

app = FastAPI()
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
def brasil(request: Request):
    return templates.TemplateResponse('brasil.html', {
        'request': request
    })

@app.get("/portugal")
def portugal(request: Request, distrito=None, municipio=None, freguesia=None, db:Session = Depends(get_db)):
    
    places = db.query(Portugal.index_label).all()
    
    if distrito:
        crud.get_portugal_distrito(db, distrito)
    
    if municipio:
        crud.get_portugal_municipio(db, municipio)
    
    if freguesia:
        crud.get_portugal_freguesia(db, freguesia)
    
    crud.get_local_portugal(db)
    
    return templates.TemplateResponse('portugal.html', {
        'request': request,
        'places': places,
        'distrito': distrito,
        'municipio': municipio,
        'freguesia': freguesia
    })
