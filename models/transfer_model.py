from sqlalchemy import Column, Integer, String
from core.configs import settings



class TransferModel(settings.DBBaseModel):
    __tablename__ = 'transfer'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    friend_id = Column(String)
    total_to_transfer = Column(Integer)
    billing_card = Column(String)

