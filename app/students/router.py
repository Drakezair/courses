from fastapi import APIRouter, Depends
from .schema import StudentSchema
from db import get_db
from sqlalchemy.orm import Session
from .model import Student


router = APIRouter()

@router.get("/")
def get_students(db: Session = Depends(get_db)):
  return db.query(Student).all()

@router.get("/{student_id}")
def get_student(student_id: int ,db: Session = Depends(get_db)):
  return db.query(Student).filter(Student.id == student_id).first()

@router.post("/")
async def create_student(student: StudentSchema, db: Session = Depends(get_db)):
    new_student = Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
    

@router.put("/{student_id}")
def update_student(student_id: int, student: StudentSchema, db: Session = Depends(get_db)):
    db.query(Student).filter(Student.id == student_id).update(student.dict())
    db.commit()
    return db.query(Student).filter(Student.id == student_id).first()
  
@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db.query(Student).filter(Student.id == student_id).delete()
    db.commit()
    return {"message": "Student deleted successfully!"}