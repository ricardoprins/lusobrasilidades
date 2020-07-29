from sqlalchemy import Column, Integer, Text
from .database import Base
class Portugal(Base):
    __tablename__ = "portugal"
    
    index_label = Column(Integer, primary_key=True, index=True)
    distrito = Column(Text, index=True)
    municipio = Column(Text, index=True)
    freguesia = Column(Text, index=True)
class Brasil(Base):
    __tablename__ = "brasil"
    
    index_label = Column(Integer, primary_key=True, index=True)
    estado = Column(Text, index=True)
    municipio = Column(Text, index=True)

    