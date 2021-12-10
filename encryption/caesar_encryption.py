import logging
import random
import string

from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from model.models import EncryptedString

logger = logging.getLogger(__name__)

SqlAlchemyBase = declarative_base()
engine = create_engine("sqlite:///data.db", echo=True)


class CaesarEncryption(SqlAlchemyBase):

    __tablename__ = "caesar_encryption"

    id = Column(Integer, primary_key=True)
    shift = Column(Integer)

    #encrypted_strings = relationship("EncryptedString", back_populates="encrypt_type")

    def __init__(self):
        self.alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        self.shift = ""
        self.user_input = ""
        SqlAlchemyBase.metadata.create_all(engine)

    def encrypt_input(self, user_input):
        shift = self.get_shift_value()
        # session.add(shift)
        # session.commit()
        encrypted_string = EncryptedString(user_input)

        for pos in range(len(user_input)):
            if user_input[pos] == " ":
                encrypted_string.content_list[pos] = " "
            elif user_input[pos] == "~":
                encrypted_string.content_list[pos] = self.alphabet[0]
            else:
                y = self.alphabet.index(user_input[pos])

                if y + shift > len(self.alphabet):
                    rest = shift % len(self.alphabet)
                    difference = len(self.alphabet) - y
                    rest = rest - difference
                    encrypted_string.content_list[pos] = self.alphabet[rest]
                else:
                    encrypted_string.content_list[pos] = self.alphabet[y + shift]

        encrypted_string = "".join(encrypted_string.content_list)
        return encrypted_string

    def get_shift_value(self):
        self.shift = input("Please insert the offset/vector (Press Enter for a random value): ")
        if self.shift == "":
            self.shift = random.randint(0, 1024)
            logger.info(f"User chose shift of {self.shift} ")
        else:
            logger.info(f"User chose shift of {self.shift}")
        try:
            return int(self.shift)
        except ValueError:
            return self.shift

    def get_user_input_from_cli(self):
        self.user_input = input()
        try:
            self.validate_input(self.user_input)
        except ValueError as error:
            logger.info(error)
            self.get_user_input_from_cli()
        return self.user_input

    def validate_input(self, user_input):
        for char in user_input:
            if char not in self.alphabet and char != " ":
                raise ValueError("Sorry, only no special characters allowed. Please try again.")



