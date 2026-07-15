from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.student import StudentCreate,StudentResponse
from app.services.student_service import StudentService

from app.schemas.student import StudentUpdate
from uuid import UUID
from fastapi import HTTPException,status

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

student_service = StudentService()

@router.post(
    "/",
    response_model = StudentResponse,
    status_code = status.HTTP_201_CREATED
)

def create_student(
    student:StudentCreate,
    db:Session = Depends(get_db)
):
    return student_service.create_student(db,student)

@router.get("/",response_model=list[StudentResponse])
def get_students(db:Session = Depends(get_db)):
    return student_service.get_all_students(db)

@router.put("/{student_id}",response_model=StudentResponse)
def update_student(student_id:UUID,student:StudentUpdate,db:Session = Depends(get_db),):
    updated_student = student_service.update_student(db, student_id, student)
    if updated_student is None:
        raise HTTPException(
            status_code=404,
            detail = "Student Not Found"
        )
    return updated_student

@router.delete("/{student_id}",status_code=status.HTTP_200_OK)
def delete_student(student_id:UUID,db:Session = Depends(get_db)):
    student = student_service.delete_student(db,student_id)
    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    return {
        'message':'student delete successfully'
    }
