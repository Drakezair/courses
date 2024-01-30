from typing import Optional
from pydantic import BaseModel

class RoomSchema(BaseModel):
    _id: Optional[int]
    name: str
    group_id: int
    teacher_id: int