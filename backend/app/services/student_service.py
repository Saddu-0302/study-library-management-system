from sqlalchemy.orm import Session
from app.models.student import Student
from app.repository.student_repository import StudentRepository
from app.schemas.student import StudentCreate,StudentUpdate
from uuid import UUID


class StudentService:
    def __init__(self):
        self.repository = StudentRepository()
    
    def create_student(self,db:Session,student:StudentCreate):
        new_student = Student(**student.model_dump())
        return self.repository.create(db,new_student)

    def get_all_students(self,db:Session):
        return self.repository.get_all(db)

    def update_student(self,db:Session,student_id:UUID,student_data:StudentUpdate):
        student = self.repository.get_by_id(db,student_id)
        if not student:
            return None
        update_data = student_data.model_dump(exclude_unset=True)
        for key,value in update_data.items():
            setattr(student, key, value)
        return self.repository.update(db, student)
    
    def delete_student(self,db:Session,student_id:UUID):
        student = self.repository.get_by_id(db,student_id)
        if not student:
            return None
        student.is_active = False
        return self.repository.update(db,student)