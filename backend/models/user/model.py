import pydantic


class User(pydantic.BaseModel):
    name: str = ""
    email: pydantic.EmailStr
    telephone: str = ""
    jwt_token: str = ""
    temp_pass: str