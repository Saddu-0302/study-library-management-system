from sqlalchemy import Boolean, Enum, Integer
from sqlalchemy.orm import Mapped,mapped_column

from app.core.constants import SeatStatus
from app.database.base_class import BaseModel

class Seat(BaseModel):
    __tablename__ = "seats"

    seat_number:Mapped[int] = mapped_column(
        Integer,
        unique=True,
        nullable=False
    )
    status:Mapped[SeatStatus] = mapped_column(
        Enum(SeatStatus),
        default = SeatStatus.AVAILABLE
    )
    is_active:Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )