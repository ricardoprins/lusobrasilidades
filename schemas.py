from pydantic import BaseModel

class PortugalRead(BaseModel):
    index_label: int
    distrito: str
    municipio: str
    freguesia: str
    
    class Config:
        orm_mode = True
    
class BrasilRead(BaseModel):
    index_label: int
    estado: str
    municipio: str
    
    class Config:
        orm_mode = True 