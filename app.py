from flask import Flask, redirect, url_for, render_template
import logging, sys
from menu.menu import Menu
from user.user import User
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker


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
        userName = input("Please insert your name to login: ")
        user = User(userName)
        session.add(user)
        logger.info(f"User with name {user.name} created")
        session.commit()
        logger.info("Session committed")


    def create_menu(self):
        self.menu = Menu()


    def keep_encryption_alive(self):
        while True:
            encryption = self.menu.define_encryption_type_or_exit()
            print("Please insert a string ")
            encryption.get_userInput_from_cli()
            encryption.encrypt_input(encryption.userInput)
            print(encryption.encryptedContent)


if __name__ == "__main__":
    app = App()
    app.start()
    app.create_menu()
    app.keep_encryption_alive()







    
