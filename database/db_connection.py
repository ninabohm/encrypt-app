import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

logger = logging.getLogger(__name__)

def connect_to_db():
    SqlAlchemyBase = declarative_base()
    engine = create_engine("sqlite:///data.db")
    logger.info("Engine created")
    SqlAlchemyBase.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    logger.info("DB session started")

if __name__ == '__main__':
    connect_to_db()

