import pydantic
from cuid import cuid


class User(pydantic.BaseModel):
    id: str = ""
    name: str
    email: pydantic.EmailStr = ""
    telephone: str = ""

    class Config:
        orm_mode = True

    @pydantic.validator("id", pre=True, always=True)
    def default_id(cls, v):
        if v:
            return v
        return cuid()
