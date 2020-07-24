from sqlalchemy import Column, Integer, String
from database import Base

class Portugal(Base):
    __tablename__ = "portugal"
    
    id = Column(Integer, primary_key=True, index=True)
    distrito = Column(String, index=True)
    municipio = Column(String, index=True)
    freguesia = Column(String, index=True)
    
class Brasil(Base):
    __tablename__ = "brasil"
    
    id = Column(Integer, primary_key=True, index=True)
    estado = Column(String, index=True)
    municipio = Column(String, index=True)
    
    