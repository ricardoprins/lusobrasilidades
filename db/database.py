import os
from . import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
DB Configuration
File, engine, session and base
"""


def enginemaker():
    try:
        A = os.environ.get('DATABASE_URL')        
        engine = create_engine(A)
    except:
        A = config.DB_URI
        engine = create_engine(A)
    return engine


engine = enginemaker()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
