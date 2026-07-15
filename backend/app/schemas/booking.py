from datetime import datetime,date
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel,ConfigDict,Field
from app.core.constants import BookingStatus, PaymentStatus

class BookingCreate(BaseModel):
    student_id:UUID
    seat_number:  int = Field(gt=0,le=300)
    start_date:date
    months:Field(gt=0,le=12)
    amount:Decimal

class BookingResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id:UUID
    student_id:UUID
    seat_id:UUID
    start_date:date
    end_date:date
    amount:Decimal
    payment_status:PaymentStatus
    booking_status:BookingStatus
    created_at:datetime
    updated_at:datetime