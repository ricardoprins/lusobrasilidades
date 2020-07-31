import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


"""
DB Configuration
File, engine, session and base
"""

# DATABASE_URL = 'postgres://lmkbmpjehkurvv:4662b55666124d08087aa6547c3b1597dcd845c995cd6a65fdb5ecb3ee96b453@ec2-3-215-83-17.compute-1.amazonaws.com:5432/d1g9c93mj67gr3'

engine = create_engine(os.environ.get('DATABASE_URL'))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
