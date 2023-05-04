from typing import Optional

from pydantic import BaseModel as SCBaseModel


class TransferSchema(SCBaseModel):
    id: Optional[int]
    friend_id: str
    total_to_transfer: int
    billing_card: str
