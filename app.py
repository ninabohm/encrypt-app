import logging, sys
from menu.menu import Menu
from models import User
from models import EncryptedString
from models import EncryptionBase
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.exc import IntegrityError


logging.basicConfig(stream=sys.stdout,
                    encoding="utf-8",
                    level=logging.DEBUG,
                    format="%(asctime)s %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")

logger = logging.getLogger(__name__)


def set_user():
    user_name = input("First name: ")
    password = input("Password: ")
    try:
        user = check_if_username_and_password_match(user_name, password)
    except NoResultFound:
        try:
            user = User(user_name, password)
            session.add(user)
            session.commit()
            logger.info(f"User with name {user_name} did not exist yet, created user on the fly")
        except IntegrityError:
            session.rollback()
            logger.info(f"User {user_name} already exists. Please try again.")
            set_user()
    except MultipleResultsFound:
        user = session.query(User).filter_by(name=user_name).first()
        logger.info(f"User with name {user_name} exists already more than once. Logging into first account")
    return user


def check_if_username_and_password_match(user_name: str, password: str):
    return session.query(User).filter_by(name=user_name, password=password).one()


def keep_alive():
    while True:
        try:
            encryption = menu.define_encryption_type_or_exit()
        except ValueError as error:
            logger.info(error)
            print("We don't have a menu option for this number, please try again")
            exit()
        user_input = encryption.get_user_input_from_cli()
        user_shift = encryption.get_shift_from_cli()
        encryption_content = encryption.encrypt_input(user_input, user_shift)
        session.add(encryption)

        try:
            encrypted_string = EncryptedString(encryption_content, encryption, user_curr)
            encryption.encrypted_strings.append(encrypted_string)
            session.add(encrypted_string)
            session.commit()
            print(encrypted_string.content)
        except KeyError as error:
            logger.info(f"error: {error}")


def check_if_encryption_type_exists(type: str):
    return session.query(EncryptionBase).filter_by(type=type)


if __name__ == "__main__":
    SqlAlchemyBase = declarative_base()
    engine = create_engine("sqlite:///data.db")
    SqlAlchemyBase.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    user_curr = set_user()
    menu = Menu()
    keep_alive()
    session.commit()










