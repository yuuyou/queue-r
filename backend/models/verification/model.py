import pydantic
from cuid import cuid


class Verification(pydantic.BaseModel):
    id: str = ""
    email: pydantic.EmailStr
    temp_pass: str

    class Config:
        orm_mode = True

    @pydantic.validator("id", pre=True, always=True)
    def default_id(cls, v):
        if v:
            return v
        return cuid()