from sqlalchemy.orm import Session
from sqlalchemy import func
from .model import Queue as QueueModel
from .schema import Queue as QueueSchema

def create_queue(db: Session, queue: QueueModel):
    db_queue = QueueSchema(**queue.dict())
    db.add(db_queue)
    db.commit()
    db.refresh(db_queue)
    return db_queue

def update_queue(db: Session, queue: QueueModel):
    db_queue = (
        db.query(QueueModel).filter(QueueModel.id == queue.id).first().update(**queue.dict())
    )

    db.commit()
    db.refresh(db_queue)
    return db_queue