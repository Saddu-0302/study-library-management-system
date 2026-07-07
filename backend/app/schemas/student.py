from pydantic import BaseModel,ConfigDict,EmailStr

class StudentCreate(BaseModel):
    full_name : str
    phone : str
    email :EmailStr

class StudentUpdate(BaseModel):
    full_name : str | None = None
    phone : str | None = None
    email : EmailStr | None = None

