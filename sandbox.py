from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

SqlAlchemyBase = declarative_base()




class TestString(SqlAlchemyBase):

    __tablename__ = "test"

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)

    def __init__(self, content):
        self.content = content



class TestString2(SqlAlchemyBase):

    __tablename__ = "test2"

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)

    def __init__(self, content):
        self.content = content


if __name__ == '__main__':
    engine = create_engine("sqlite:///data.db")
    SqlAlchemyBase.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    testy = TestString("Käsekuchen")
    session.add(testy)
    session.commit()
    dictionary = dict(session.query(TestString.id, TestString.content))
