from core.configs import settings

from sqlalchemy import Column, Integer, String, ForeignKey


class BankStatementModel(settings.DBBaseModel):
    __tablename__ = 'bank_statement'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    user_id: int = Column(Integer, ForeignKey('persons.id'))
    friend_id: int = Column(Integer, ForeignKey('friends.id'))
    value: int = Column(Integer)
    from_card: str = Column(String(100))
