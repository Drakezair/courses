from typing import Optional
from pydantic import BaseModel

class StudentSchema(BaseModel):
    _id: Optional[int]
    first_name: str
    last_name: str
    email: str
    guardian_id: Optional[str]
