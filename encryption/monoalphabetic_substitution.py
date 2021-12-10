from model.models import EncryptedString
import string
import logging
from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base

logger = logging.getLogger(__name__)

SqlAlchemyBase = declarative_base()
engine = create_engine("sqlite:///data.db", echo=True)


class MonoalphabeticSubstitution(SqlAlchemyBase):

    __tablename__ = "caesar_encryption"

    id = Column(Integer, primary_key=True)
    shift = Column(Integer)

    def __init__(self):
        self.alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        self.user_input = ""

    def encrypt_input(self, user_input):
        encrypted_string = EncryptedString(user_input)
        for pos in range(len(user_input)):
            if user_input[pos] == " ":
                encrypted_string.content_list[pos] = " "
            else: 
                left = self.alphabet.index(user_input[pos])
                right = len(self.alphabet) - 1 - left
                encrypted_string.content_list[pos] = self.alphabet[right]

        encrypted_string = "".join(encrypted_string.content_list)
        return encrypted_string

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
