import pydantic 
from cuid import cuid
from enum import Enum

class QueueStatus(str, Enum):
    waiting = 'waiting'
    reminded = 'reminded'
    cancelled = 'cancelled'
    completed = 'completed'


class Queue(pydantic.BaseModel):
    id: str = ""
    store_id: str
    user_id: str
    queue_number: int
    number_of_people: int
    queue_status: QueueStatus = QueueStatus.waiting

    class Config:
        orm_mode = True
    
    @pydantic.validator("id", pre=True, always=True)
    def default_id(cls, v):
        if v:
            return v
        return cuid()