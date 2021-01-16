import pydantic
from cuid import cuid

class Store(pydantic.BaseModel):
    id: str = ""
    owner_id: str
    name: str

    class Config:
        orm_mode = True

    @pydantic.validator("id", pre=True, always=True)
    def default_id(cls, v):
        if v:
            return v
        return cuid()
    