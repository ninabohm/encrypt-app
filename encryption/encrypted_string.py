from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


SqlAlchemyBase = declarative_base()


class EncryptedString(SqlAlchemyBase):

    __tablename__ = "encrypted_string"

    id = Column(Integer, primary_key=True)
    content = Column(String)
    # user_id = Column(Integer, ForeignKey("user.id"))

    def __init__(self, user_input: str):
        self.content = list(user_input)

