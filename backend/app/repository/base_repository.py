from typing import Generic,TypeVar,Type
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")

class BaseRepository(Generic[ModelType]):
    def __init__(self,model:Type[ModelType]):
        self.model = model
    
    def get_by_id(self,db:Session,obj_id):
        return db.get(self.model,obj_id)

    def get_all(self,db:Session):
        return db.query(self.model).all()
    
    def create(self,db:Session,obj):
        db.add(obj)
        return obj
    
    def delete(self,db:Session,obj):
        db.delete(obj)

    def update(self,db:Session,obj):
         return obj
    
