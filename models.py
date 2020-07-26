from sqlalchemy import Column, Integer, String
from database import Base

class Portugal(Base):
    __tablename__ = "portugal"
    
    index_label = Column(Integer, primary_key=True, index=True)
    distrito = Column(String, index=True)
    municipio = Column(String, index=True)
    freguesia = Column(String, index=True)
    
class Brasil(Base):
    __tablename__ = "brasil"
    
    index_label = Column(Integer, primary_key=True, index=True)
    estado = Column(String, index=True)
    municipio = Column(String, index=True)
    
    