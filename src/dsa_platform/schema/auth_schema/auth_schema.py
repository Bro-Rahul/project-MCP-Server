from pydantic import BaseModel, EmailStr


class RegisterSchema(BaseModel):

    username: str
    password: str
    email: EmailStr


class LoginSchema(BaseModel):

    email: str
    password: str


class LoginResponseSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    access: str
    isAdmin: bool
