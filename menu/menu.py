from model.models import CaesarEncryption
from model.models import MonoalphabeticSubstitution
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SqlAlchemyBase = declarative_base()
engine = create_engine("sqlite:///data.db")


class Menu:

    def __init__(self):
        self.print_menu()
        self.option = input("Choose a value and press Enter: ")

    @staticmethod
    def print_menu():
        print("Welcome to the encrypt-app")
        print("1: Caesar Encryption")
        print("2: Monoalphabetic Substitution Encryption")
        print("3: About")
        print("4: Quit program")

    def define_encryption_type_or_exit(self):
        SqlAlchemyBase.metadata.create_all(engine)
        Session = sessionmaker(engine)
        session = Session()

        if self.option == "1":
            encryption = CaesarEncryption()
            session.add(encryption)
            session.commit()
            return encryption

        if self.option == "2":
            encryption = MonoalphabeticSubstitution()
            session.add(encryption)
            session.commit()
            return encryption

        if self.option == "3":
            print("Learn more about the app on https://gitlab.rz.htw-berlin.de/schroedr/vl2022_ina/")

        if self.option == "4":
            exit()



