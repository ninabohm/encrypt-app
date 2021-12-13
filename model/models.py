import random
import string
import logging

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

logger = logging.getLogger(__name__)

SqlAlchemyBase = declarative_base()
engine = create_engine("sqlite:///data.db", echo=True)


class User(SqlAlchemyBase):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    encrypted_strings = relationship("EncryptedString", back_populates="user")

    def __init__(self, name: str):
        self.name = name


class CaesarEncryption(SqlAlchemyBase):

    __tablename__ = "caesar_encryption"

    id = Column(Integer, primary_key=True)
    type = Column(String)
    # TODO: make type unique
    shift = Column(Integer)

    encrypted_strings = relationship("EncryptedString", back_populates="encryption_type")

    def __init__(self):
        self.alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        self.type = "caesar"
        self.shift = 0
        SqlAlchemyBase.metadata.create_all(engine)

    def encrypt_input(self, user_input, user_shift):
        self.shift = user_shift
        encrypted_string = "käsekuchen"
        # encrypted_string = EncryptedString(user_input, self.type)
        # # TODO: this encrypted string is the cause of the double generation in the db, remove it
        #
        # for pos in range(len(user_input)):
        #     if user_input[pos] == " ":
        #         encrypted_string.content_list[pos] = " "
        #     elif user_input[pos] == "~":
        #         encrypted_string.content_list[pos] = self.alphabet[0]
        #     else:
        #         y = self.alphabet.index(user_input[pos])
        #
        #         if y + self.shift > len(self.alphabet):
        #             rest = self.shift % len(self.alphabet)
        #             difference = len(self.alphabet) - y
        #             rest = rest - difference
        #             encrypted_string.content_list[pos] = self.alphabet[rest]
        #         else:
        #             encrypted_string.content_list[pos] = self.alphabet[y + self.shift]
        #
        # encrypted_string = "".join(encrypted_string.content_list)
        return encrypted_string

    def get_user_input_from_cli(self):
        print("Please insert a string ")
        user_input = input()
        try:
            self.validate_input(user_input)
        except ValueError as error:
            logger.info(error)
            self.get_user_input_from_cli()
        return user_input

    def validate_input(self, user_input):
        for char in user_input:
            if char not in self.alphabet and char != " ":
                raise ValueError("Sorry, only no special characters allowed. Please try again.")

    def get_shift_value(self):
        shift_value = input("Please insert the offset/vector (Press Enter for a random value): ")
        if shift_value == "":
            shift_value = random.randint(0, 1024)
            logger.info(f"User chose shift of {shift_value} ")
        else:
            try:
                shift_value = int(shift_value)
                logger.info(f"User chose shift of {shift_value}")
                return shift_value
            except ValueError:
                shift_value = int(shift_value)
                logger.info(f"User chose shift of {shift_value}")
                return shift_value


class EncryptedString(SqlAlchemyBase):

    __tablename__ = "encrypted_string"

    id = Column(Integer, primary_key=True)
    content = Column(String)

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="encrypted_strings")

    encryption_type_id = Column(Integer, ForeignKey("caesar_encryption.id"))
    encryption_type = relationship("CaesarEncryption", back_populates="encrypted_strings")

    def __init__(self, input_string, encryption_type):
        self.content_list = list(input_string)
        self.content = "".join(self.content_list)
        self.encryption_type = encryption_type


SqlAlchemyBase.metadata.create_all(engine)
