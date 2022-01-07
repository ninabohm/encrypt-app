import random
import string
import logging

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


logger = logging.getLogger(__name__)

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    encrypted_strings = db.relationship("EncryptedString", back_populates="user")

    def __init__(self, name: str):
        self.name = name


class EncryptionBase(db.Model):

    __tablename__ = "encryption_base"

    id = db.Column(Integer, primary_key=True)
    type = db.Column(String)
    shift = db.Column(Integer)
    encrypted_strings = db.relationship("EncryptedString", back_populates="encryption_base")

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'encryption_base'
    }

    def __init__(self):
        self.alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    def get_user_input_from_cli(self):
        user_input = input("Please insert a string ")
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


class CaesarEncryption(EncryptionBase):

    __mapper_args__ = {
        'polymorphic_identity': 'caesar'
    }

    def __init__(self):
        super().__init__()
        self.type = "caesar"
        self.shift = 0

    def encrypt_input(self, user_input, user_shift):
        self.shift = user_shift
        encrypted_string = list(user_input)

        for pos in range(len(user_input)):
            if user_input[pos] == " ":
                encrypted_string[pos] = " "
            elif user_input[pos] == "~":
                encrypted_string[pos] = self.alphabet[0]
            else:
                y = self.alphabet.index(user_input[pos])

                if y + self.shift > len(self.alphabet):
                    rest = self.shift % len(self.alphabet)
                    difference = len(self.alphabet) - y
                    rest = rest - difference
                    encrypted_string[pos] = self.alphabet[rest]
                else:
                    encrypted_string[pos] = self.alphabet[y + self.shift]

        encrypted_string = "".join(encrypted_string)
        return encrypted_string

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


class MonoalphabeticSubstitution(EncryptionBase):

    __mapper_args__ = {
        'polymorphic_identity': 'monoalphabetic_substitution'
    }

    def __init__(self):
        super().__init__()
        self.type = "monoalphabetic_substitution"

    def encrypt_input(self, user_input, user_shift):
        encrypted_string = list(user_input)
        for pos in range(len(user_input)):
            if user_input[pos] == " ":
                encrypted_string[pos] = " "
            else:
                left = self.alphabet.index(user_input[pos])
                right = len(self.alphabet) - 1 - left
                encrypted_string[pos] = self.alphabet[right]

        encrypted_string = "".join(encrypted_string)
        return encrypted_string

    def get_shift_value(self):
        return 0


class EncryptedString(db.Model):

    __tablename__ = "encrypted_string"

    id = db.Column(Integer, primary_key=True)
    content = db.Column(String)
    encryption_type = db.Column(String)

    encryption_base_id = db.Column(ForeignKey("encryption_base.id"))
    encryption_base = db.relationship("EncryptionBase", back_populates="encrypted_strings", uselist=False)

    user_id = db.Column(Integer, ForeignKey("user.id"))
    user = db.relationship("User", back_populates="encrypted_strings", uselist=False)

    def __init__(self, input_string: str, encryption, user):
        self.content_list = list(input_string)
        self.content = "".join(self.content_list)
        self.encryption_base = encryption
        self.encryption_type = encryption.type
        self.user = user
