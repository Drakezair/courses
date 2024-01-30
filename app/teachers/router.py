from fastapi import APIRouter, Depends
from .schema import TeacherSchema
from db import get_db
from sqlalchemy.orm import Session
from .model import Teacher


router = APIRouter()

@router.get("/")
def get_teachers(db: Session = Depends(get_db)):
  return db.query(Teacher).all()

@router.get("/{teacher_id}")
def get_teacher(teacher_id: int ,db: Session = Depends(get_db)):
  return db.query(Teacher).filter(Teacher.id == teacher_id).first()

@router.post("/")
async def create_teacher(teacher: TeacherSchema, db: Session = Depends(get_db)):
    new_teacher = Teacher(**teacher.dict())
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher

@router.put("/{teacher_id}")
def update_teacher(teacher_id: int, room: TeacherSchema, db: Session = Depends(get_db)):
    db.query(Teacher).filter(Teacher.id == teacher_id).update(room.dict())
    db.commit()
    return db.query(Teacher).filter(Teacher.id == teacher_id).first()
  
@router.delete("/{teacher_id}")
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    db.query(Teacher).filter(Teacher.id == teacher_id).delete()
    db.commit()
    return {"message": "RTeacheroom deleted successfully!"}