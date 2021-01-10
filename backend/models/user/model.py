import pydantic


class Verification(pydantic.BaseModel):
    name: str
    email: pydantic.EmailStr
    telephone: str