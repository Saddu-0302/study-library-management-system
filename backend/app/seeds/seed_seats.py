from app.database.session import SessionLocal
from app.models.seat import Seat
from app.core.constants import SeatStatus

db = SessionLocal()

try:
    if db.query(Seat).count() > 0:
        print("Seat already exist")
    else:
        seats = []
        for i in range(1,301):
            seat = Seat(
                seat_number = i,
                status = SeatStatus.AVAILABLE
            )
            seats.append(seat)
        db.add_all(seats)
        db.commit()
        print('300 Seats created successfully')
finally:
    db.close()