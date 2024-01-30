from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from db import Base

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, index=True, unique=True)
    guardian_id = Column(Integer)