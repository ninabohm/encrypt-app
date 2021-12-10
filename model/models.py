from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

SqlAlchemyBase = declarative_base()
engine = create_engine("sqlite:///data.db", echo=True)


class User(SqlAlchemyBase):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    encrypted_strings = relationship("EncryptedString", back_populates="user")

    def __init__(self, name: str):
        self.name = name


class EncryptedString(SqlAlchemyBase):

    __tablename__ = "encrypted_string"

    id = Column(Integer, primary_key=True)
    content = Column(String)

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="encrypted_strings")

    def __init__(self, input_string: str):
        self.content_list = list(input_string)
        self.content = "".join(self.content_list)


SqlAlchemyBase.metadata.create_all(engine)
