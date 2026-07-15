from datetime import datetime
from uuid import UUID

from pydantic import BaseModel,ConfigDict,EmailStr

class StudentCreate(BaseModel):
    full_name : str
    phone : str
    email :EmailStr

class StudentUpdate(BaseModel):
    full_name : str | None = None
    phone : str | None = None
    email : EmailStr | None = None

class StudentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    full_name:str
    phone:str
    email:EmailStr
    is_active:bool
    created_at:datetime
    updated_at:datetime