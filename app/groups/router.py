from fastapi import APIRouter, Depends
from .schema import GroupSchema
from db import get_db
from sqlalchemy.orm import Session
from .model import Group


router = APIRouter()

@router.get("/")
def get_groups(db: Session = Depends(get_db)):
  return db.query(Group).all()

@router.get("/{group_id}")
def get_group(group_id: int ,db: Session = Depends(get_db)):
  return db.query(Group).filter(Group.id == group_id).first()

@router.post("/")
async def create_group(group: GroupSchema, db: Session = Depends(get_db)):
    new_group = Group(**group.dict())
    db.add(new_group)
    db.commit()
    db.refresh(new_group)
    return new_group
    

@router.put("/{group_id}")
def update_group(group_id: int, group: GroupSchema, db: Session = Depends(get_db)):
    db.query(Group).filter(Group.id == group_id).update(group.dict())
    db.commit()
    return db.query(Group).filter(Group.id == group_id).first()
  
@router.delete("/{group_id}")
def delete_group(group_id: int, db: Session = Depends(get_db)):
    db.query(Group).filter(Group.id == group_id).delete()
    db.commit()
    return {"message": "Guardians deleted successfully!"}