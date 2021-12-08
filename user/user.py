import logging
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


logger = logging.getLogger(__name__)
SqlAlchemyBase = declarative_base()


class User(SqlAlchemyBase):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    # encrypted_strings = relationship("EncryptedString")

    def __init__(self, name: str):
        self.name = name
