from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.configs import settings


class TransferModel(settings.DBBaseModel):
    __tablename__ = 'billing_card'

    id = Column(Integer, primary_key=True)
    card_id = Column(String)

    transfer = relationship("Transfer", uselist=False, back_populates="billing_card")


class Transfer(settings.DBBaseModel):
    __tablename__ = 'transfer'

    id = Column(Integer, primary_key=True)
    friend_id = Column(String)
    total_to_transfer = Column(Integer)

    billing_card_id = Column(Integer, ForeignKey('billing_card.id'))
    billing_card = relationship("BillingCard", back_populates="transfer")

    def to_dict(self):
        """
            The to_dict method in Transfer is a helper method to convert the
            database model to the desired JSON format.
        """
        return {
            'friend_id': self.friend_id,
            'total_to_transfer': self.total_to_transfer,
            'billing_card': {
                'card_id': self.billing_card.card_id
            }
        }
