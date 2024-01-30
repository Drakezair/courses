from typing import Optional
from pydantic import BaseModel

class CourseSchema(BaseModel):
    _id: Optional[int]
    name: str
    description: Optional[str]
