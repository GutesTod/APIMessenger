from pydantic import BaseModel

class UserBase(BaseModel):
    pass

class UserCreate(UserBase):
    username: str
    password: str
    
class UserGet(UserCreate):
    pass

class UserDelete(UserBase):
    id: int
    
class UserResponse(UserBase):
    id: int
    username: str
    password: str