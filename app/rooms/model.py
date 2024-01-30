from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import String, BigInteger, Integer
from db import Base

class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    group_id = Column(Integer, index=True)
    teacher_id = Column(Integer, index=True)