from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import String, BigInteger, Integer
from db import Base

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String, nullable=True)