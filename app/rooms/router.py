from fastapi import APIRouter, Depends
from .schema import RoomSchema
from db import get_db
from sqlalchemy.orm import Session
from .model import Room


router = APIRouter()

@router.get("/")
def get_rooms(db: Session = Depends(get_db)):
  return db.query(Room).all()

@router.get("/{room_id}")
def get_room(room_id: int ,db: Session = Depends(get_db)):
  return db.query(Room).filter(Room.id == room_id).first()

@router.post("/")
async def create_room(room: RoomSchema, db: Session = Depends(get_db)):
    new_room = Room(**room.dict())
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return new_room

@router.put("/{room_id}")
def update_room(room_id: int, room: RoomSchema, db: Session = Depends(get_db)):
    db.query(Room).filter(Room.id == room_id).update(room.dict())
    db.commit()
    return db.query(Room).filter(Room.id == room_id).first()
  
@router.delete("/{room_id}")
def delete_room(room_id: int, db: Session = Depends(get_db)):
    db.query(Room).filter(Room.id == room_id).delete()
    db.commit()
    return {"message": "Room deleted successfully!"}