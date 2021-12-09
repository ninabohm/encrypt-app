from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base


SqlAlchemyBase = declarative_base()
engine = create_engine("sqlite:///data.db", echo=True)


class EncryptedString(SqlAlchemyBase):

    __tablename__ = "encrypted_string"

    id = Column(Integer, primary_key=True)
    content = Column(String)

    def __init__(self, input_string: str):
        self.content_list = list(input_string)
        self.content = "".join(self.content_list)


SqlAlchemyBase.metadata.create_all(engine)