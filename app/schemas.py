from pydantic import BaseModel, EmailStr
from datetime import datetime
# pydantic schema

# User --> API
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

# API --> User
class Post(PostBase):
    # the other 3 are being automatically inherited
    id: int
    created_at: datetime
    # To let the input convert into a dict format
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    # This allows pydantic to convert the SQLALCHEMY model into readable dict
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
