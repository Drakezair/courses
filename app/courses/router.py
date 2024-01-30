from fastapi import APIRouter, Depends
from .schema import CourseSchema
from db import get_db
from sqlalchemy.orm import Session
from .model import Course


router = APIRouter()

@router.get("/")
def get_courses(db: Session = Depends(get_db)):
  return db.query(Course).all()

@router.get("/{course_id}")
def get_course(course_id: int ,db: Session = Depends(get_db)):
  return db.query(Course).filter(Course.id == course_id).first()

@router.post("/")
async def create_course(course: CourseSchema, db: Session = Depends(get_db)):
    new_course = Course(**course.dict())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

@router.put("/{course_id}")
def update_course(course_id: int, course: CourseSchema, db: Session = Depends(get_db)):
    db.query(Course).filter(Course.id == course_id).update(course.dict())
    db.commit()
    return db.query(Course).filter(Course.id == course_id).first()
  
@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db.query(Course).filter(Course.id == course_id).delete()
    db.commit()
    return {"message": "Course deleted successfully!"}