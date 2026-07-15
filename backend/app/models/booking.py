import uuid
from sqlalchemy import Column,Date,ForeignKey,Numeric,Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.base import Base
from app.core.constants import BookingStatus,PaymentStatus
from app.models.mixins import TimestampMixin

class Booking(Base,TimestampMixin):
    __tablename__ = "bookings"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    student_id= Column(
        UUID(as_uuid=True),
        ForeignKey("students.id"),
        nullable=False
    )
    seat_id= Column(
        UUID(as_uuid=True),
        ForeignKey('seats.id'),
        nullable=False
    )
    start_date = Column(Date,nullable=False)
    end_date =Column(Date,nullable=False)
    amount = Column(Numeric(10,2),nullable=False)
    payment_status = Column(
        Enum(PaymentStatus),
        default = PaymentStatus.PENDING,
        nullable = False
    )
    booking_status=Column(
        Enum(BookingStatus),
        default = BookingStatus.ACTIVE,
        nullable = False
    )
    student = relationship("Student",back_populates="bookings")
    seat = relationship("Seat",back_populates="bookings")