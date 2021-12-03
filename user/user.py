from user.user_list import user_list
import logging
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker


logger = logging.getLogger(__name__)
SqlAlchemyBase = declarative_base()

class User(SqlAlchemyBase):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __init__(self, name: str):
        self.logged_in = False
        self.name = name



#     user = User(self.name)
#     session.add(user)
#     logger.info('User created')
#     session.commit()
#     logger.info("Session committed")