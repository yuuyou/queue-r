import pydantic


class User(pydantic.BaseModel):
    email: pydantic.EmailStr
    temp_pass: str