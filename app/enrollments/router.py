from fastapi import APIRouter, Depends
from .schema import EnrollmentSchema
from db import get_db
from sqlalchemy.orm import Session
from .model import Enrollment


router = APIRouter()

@router.get("/")
def get_enrollments(db: Session = Depends(get_db)):
  return db.query(Enrollment).all()

@router.get("/{enrollment_id}")
def get_enrollment(enrollment_id: int ,db: Session = Depends(get_db)):
  return db.query(Enrollment).filter(Enrollment.id == enrollment_id).first()

@router.post("/")
async def create_enrollment(enrollment: EnrollmentSchema, db: Session = Depends(get_db)):
    new_enrollment = Enrollment(**enrollment.dict())
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)
    return new_enrollment

@router.put("/{enrollment_id}")
def update_enrollment(enrollment_id: int, enrollment: EnrollmentSchema, db: Session = Depends(get_db)):
    db.query(Enrollment).filter(Enrollment.id == enrollment_id).update(enrollment.dict())
    db.commit()
    return db.query(Enrollment).filter(enrollment.id == enrollment_id).first()
  
@router.delete("/{enrollment_id}")
def delete_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    db.query(Enrollment).filter(Enrollment.id == enrollment_id).delete()
    db.commit()
    return {"message": "Renrollmentoom deleted successfully!"}