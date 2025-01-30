from pydantic import BaseModel

class DialogBase(BaseModel):
    pass

class DialogCreate(DialogBase):
    user_id1: int
    user_id2: int
    
class DialogResponse(DialogBase):
    id: int
    user_id1: int
    user_id2: int