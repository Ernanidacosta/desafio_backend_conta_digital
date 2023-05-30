from typing import Optional

from pydantic import BaseModel


class FriendSchema(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    birthday: str
    username: str
    user_id: str

    class Config:
        orm_mode = True
