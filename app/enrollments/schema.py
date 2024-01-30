from typing import Optional
from pydantic import BaseModel
from shared.schemas import DocumentTypesEnum

class EnrollmentSchema(BaseModel):
    _id: Optional[int]
    group_id: int
    student_id: int
    course_id: int
    room_id: int