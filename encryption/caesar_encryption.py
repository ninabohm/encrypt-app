from encryption.encryption_base import Encryption
from encryption.encrypted_string import EncryptedString
import random
import logging

logger = logging.getLogger(__name__)

class CaesarEncryption(Encryption):

    def get_shift_value(self):
        self.shift = input("Please insert the offset/vector (Press Enter for a random value): ")
        try:
            return int (self.shift)
        except ValueError:
            self.shift = ""
            return self.shift


    def encrypt_input(self, user_input):
        shift = self.get_shift_value()
        #self.encrypted_string = EncryptedString("")
        self.encrypted_string = list(user_input)

        if shift == "":
            shift = random.randint(0, 1024)
            logger.info(f"User chose shift of {shift} ")
        else: 
            logger.info(f"User chose shift of {shift}")
        for pos in range(len(user_input)):
            if user_input[pos] == " ":
                self.encrypted_string[pos] = " "
            elif user_input[pos] == "~":
                self.encrypted_string[pos] = self.alphabet[0]
            else:
                y = self.alphabet.index(user_input[pos])
                
                if y + shift > len(self.alphabet): 
                    rest = shift % len(self.alphabet)
                    difference = len(self.alphabet) - y
                    rest = rest - difference
                    self.encrypted_string[pos] = self.alphabet[rest]
                else: 
                    self.encrypted_string[pos] = self.alphabet[y+shift]

        self.encrypted_string = "".join(self.encrypted_string)

