from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import String, Integer
from db import Base

class Enrollment(Base):
    __tablename__ = 'enrollments'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    group_id = Column(Integer, index=True)
    student_id = Column(Integer, index=True)
    course_id = Column(Integer, index=True)
    room_id = Column(Integer, index=True)