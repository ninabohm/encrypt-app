import logging, sys
from menu.menu import Menu
from user.user import User
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound


logging.basicConfig(stream=sys.stdout,
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")


logger = logging.getLogger(__name__)


SqlAlchemyBase = declarative_base()
engine = create_engine("sqlite:///data.db")
logger.info("Engine created")
SqlAlchemyBase.metadata.create_all(engine)
Session = sessionmaker(engine)
session = Session()
logger.info("DB session started")


class App:

    def start(self):
        logging.info("Application up and running")
        user_name = input("Please insert your name to login. You'll be registered automatically if you have no account yet.: ")
        user = User(user_name)
        try:
            self.check_if_user_exists(user_name)
            logger.info(f"Login for user {user_name} successful")
        except NoResultFound:
            logger.info(f"User with name {user_name} does not exist yet, creating user on the fly")
            session.add(user)
            logger.info(f"User with name {user.name} created")
            session.commit()
        except MultipleResultsFound as error:
            logger.info(f"User with name {user_name} exists already more than once. Login successful.")

    def check_if_user_exists(self, user_name: str):
        return session.query(User).filter_by(name=user_name).one()

    def create_menu(self):
        self.menu = Menu()

    def keep_encryption_alive(self):
        while True:
            encryption = self.menu.define_encryption_type_or_exit()
            print("Please insert a string ")
            encryption.get_user_input_from_cli()
            encrypted_string = encryption.encrypt_input(encryption.user_input)
            print(encrypted_string)


if __name__ == "__main__":
    app = App()
    app.start()
    app.create_menu()
    app.keep_encryption_alive()







    
