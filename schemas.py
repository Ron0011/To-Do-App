from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    status: bool

    class Config:
        from_attributes = True  
