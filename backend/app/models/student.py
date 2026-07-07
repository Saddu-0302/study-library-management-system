from sqlalchemy import Boolean,String,Text
from sqlalchemy.orm import Mapped,mapped_column

from app.database.base_class import BaseModel

class Student(BaseModel):
    __tablename__ = "students"

    full_name : Mapped[str] = mapped_column(String(100),nullable=False)
    phone : Mapped[str] = mapped_column(
        String(15),
        unique=True,
        nullable=False
    )
    email:Mapped[str]= mapped_column(
        String(255),
        unique=True,
        nullable=False
    )
    address:Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )
    contact:Mapped[str | None] = mapped_column(
        String(15),
        nullable=True
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )