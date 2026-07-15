from datetime import datetime
from uuid import UUID

from pydantic import BaseModel,ConfigDict
from app.core.constants import SeatStatus

class SeatCreate(BaseModel):
    seat_number : int

class SeatUpdate(BaseModel):
    status :SeatStatus

class SeatResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    seat_number:int
    status:SeatStatus
    created_at:datetime
    updated_at:datetime