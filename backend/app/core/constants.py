from enum import Enum

class SeatStatus(str,Enum):
    AVAILABLE = "AVAILABLE"
    BOOKED = "BOOKED"
    MAINTENANCE = "MAINTENANCE"

class PaymentStatus(str,Enum):
    PAID = "PAID"
    PENDING = "PENDING"
class BookingStatus(str,Enum):
    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"
    CANCELLED = "CANCELLED"