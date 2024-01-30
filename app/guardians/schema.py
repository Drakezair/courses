from typing import Optional
from pydantic import BaseModel
from shared.schemas import DocumentTypesEnum

class GuardianSchema(BaseModel):
    _id: Optional[int]
    first_name: str
    last_name: str
    email: str
    document: Optional[str]
    document_type: Optional[DocumentTypesEnum]
    country: Optional[str]
