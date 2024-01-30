from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import String, BigInteger, Integer, DateTime
from db import Base

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String, nullable=True)
    start_time = Column(String)
    end_time = Column(String)
    course_id = Column(Integer, index=True)