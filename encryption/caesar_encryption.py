from encryption.encryption_base import Encryption
from encryption.encrypted_string import EncryptedString
import random
import logging

logger = logging.getLogger(__name__)


class CaesarEncryption(Encryption):

    def encrypt_input(self, user_input):
        shift = self.get_shift_value()
        encrypted_string = EncryptedString(user_input)

        for pos in range(len(user_input)):
            if user_input[pos] == " ":
                encrypted_string.content[pos] = " "
            elif user_input[pos] == "~":
                encrypted_string.content[pos] = self.alphabet[0]
            else:
                y = self.alphabet.index(user_input[pos])
                
                if y + shift > len(self.alphabet): 
                    rest = shift % len(self.alphabet)
                    difference = len(self.alphabet) - y
                    rest = rest - difference
                    encrypted_string.content[pos] = self.alphabet[rest]
                else: 
                    encrypted_string.content[pos] = self.alphabet[y+shift]

        encrypted_string = "".join(encrypted_string.content)
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
