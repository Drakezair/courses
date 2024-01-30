from typing import Optional
from pydantic import BaseModel


class GroupSchema(BaseModel):
    _id: Optional[int]
    name: str
    description: Optional[str]
    start_time: str
    end_time: str
    course_id: int