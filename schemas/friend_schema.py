from typing import Optional

from pydantic import BaseModel as SCBaseModel


class FriendSchema(SCBaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    birthday: str
    username: str
    user_id: str

    class Config:
        orm_mode = True
