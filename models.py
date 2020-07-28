from sqlalchemy import Column, Integer, String
from database import Base

class Portugal(Base):
    __tablename__ = "portugal"
    
    index_label = Column(Integer, primary_key=True, index=True)
    distrito = Column(String(collation='utf8_general_ci'), index=True)
    municipio = Column(String(collation='utf8_general_ci'), index=True)
    freguesia = Column(String(collation='utf8_general_ci'), index=True)
    
class Brasil(Base):
    __tablename__ = "brasil"
    
    index_label = Column(Integer, primary_key=True, index=True)
    estado = Column(String(collation='utf8_general_ci'), index=True)
    municipio = Column(String(collation='utf8_general_ci'), index=True)
    
    