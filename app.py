import logging, sys
from menu.menu import Menu
from model.models import User
from model.models import EncryptedString
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound


logging.basicConfig(stream=sys.stdout,
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

logger = logging.getLogger(__name__)


class App:

    def get_user(self):
        logging.info("Application up and running")
        user_name = input("Please login with your first name. You'll be registered automatically if you have no account yet.: ")
        try:
            self.check_if_user_exists(user_name)
            logger.info(f"Login for user {user_name} successful")
            user = session.query(User).filter_by(name=user_name).first()
            return user
        except NoResultFound:
            logger.info(f"User with name {user_name} does not exist yet, creating user on the fly")
            user = User(user_name)
            session.add(user)
            session.commit()
            logger.info(f"User with name {user.name} created")
            return user
        except MultipleResultsFound:
            logger.info(f"User with name {user_name} exists already more than once. Logging into first account")
            user = session.query(User).filter_by(name=user_name).first()
            return user

    def check_if_user_exists(self, user_name: str):
        return session.query(User).filter_by(name=user_name).one()

    def keep_alive(self):
        while True:
            encryption = menu.define_encryption_type_or_exit()
            user_input = encryption.get_user_input_from_cli()
            user_shift = encryption.get_shift_value()
            session.add(encryption)
            encryption_content = encryption.encrypt_input(user_input, user_shift)
            try:
                encrypted_string = EncryptedString(encryption_content, encryption)
                user_curr.encrypted_strings.append(encrypted_string)
                session.add(encrypted_string)
                session.commit()
                print(encrypted_string.content)
            except KeyError as error:
                print(error)


if __name__ == "__main__":
    SqlAlchemyBase = declarative_base()
    engine = create_engine("sqlite:///data.db")
    SqlAlchemyBase.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    app = App()
    user_curr = app.get_user()
    menu = Menu()
    app.keep_alive()
    session.commit()









    
