from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import String, Integer
from db import Base

class Guardians(Base):
    __tablename__ = 'guardians'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, index=True)
    document = Column(String, index=True)
    document_type = Column(String)
    country = Column(String)
    