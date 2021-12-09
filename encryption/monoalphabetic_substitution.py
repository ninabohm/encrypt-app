from encryption.encryption_base import Encryption
from encryption.encrypted_string import EncryptedString
import random, logging
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


class MonoalphabeticSubstitution(Encryption):

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
