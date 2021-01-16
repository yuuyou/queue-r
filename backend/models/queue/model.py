import pydantic 
from cuid import cuid

class Queue(pydantic.BaseModel):
    id: str = ""
    store_id: str
    user_id: str
    queue_number: int

    class Config:
        orm_mode = True
    
    @pydantic.validator("id", pre=True, always=True)
    def default_id(cls, v):
        if v:
            return v
        return cuid()