import uuid
from datetime import datetime

from sqlalchemy import DateTime,String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped,mapped_column

from app.database.base_class import BaseModel 

class User(BaseModel):
    __tablename__ = "users"

    
    email:Mapped[str]=mapped_column(
        String(255),
        unique=True,
        nullable=False
    )
    password:Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    role:Mapped[str] = mapped_column(
        String(20),
        default="admin"
    )

