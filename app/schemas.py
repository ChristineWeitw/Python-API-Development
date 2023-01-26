from pydantic import BaseModel
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
    email: str
    password: str
