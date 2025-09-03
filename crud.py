from sqlalchemy.orm import Session
import models, schemas

def get_tasks(db: Session):
    return db.query(models.Task).order_by(models.Task.id.desc()).all()

def create_task(db: Session, task: schemas.TaskCreate):
    obj = models.Task(title=task.title, status=False)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def delete_task(db: Session, task_id: int) -> bool:
    obj = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True

def update_task_status(db: Session, task_id: int):
    obj = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not obj:
        return None
    obj.status = not obj.status
    db.commit()
    db.refresh(obj)
    return obj
