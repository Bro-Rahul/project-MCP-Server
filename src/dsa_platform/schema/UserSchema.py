from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):

    username: str
    email: str
    first_name: str
    last_name: str
    avatar: Optional[str]
    id: int
