from fastapi import APIRouter, Depends
from .schema import GuardianSchema
from db import get_db
from sqlalchemy.orm import Session
from .model import Guardians


router = APIRouter()

@router.get("/")
def get_guardians(db: Session = Depends(get_db)):
  return db.query(Guardians).all()

@router.get("/{guardian_id}")
def get_guardian(guardian_id: int ,db: Session = Depends(get_db)):
  return db.query(Guardians).filter(Guardians.id == guardian_id).first()

@router.post("/")
async def create_guardian(guardian: GuardianSchema, db: Session = Depends(get_db)):
    new_guardian = Guardians(**guardian.dict())
    db.add(new_guardian)
    db.commit()
    db.refresh(new_guardian)
    return new_guardian
    

@router.put("/{guardian_id}")
def update_guardian(guardian_id: int, guardian: GuardianSchema, db: Session = Depends(get_db)):
    db.query(Guardians).filter(Guardians.id == guardian_id).update(guardian.dict())
    db.commit()
    return db.query(Guardians).filter(Guardians.id == guardian_id).first()
  
@router.delete("/{guardian_id}")
def delete_guardian(guardian_id: int, db: Session = Depends(get_db)):
    db.query(Guardians).filter(Guardians.id == guardian_id).delete()
    db.commit()
    return {"message": "Guardians deleted successfully!"}