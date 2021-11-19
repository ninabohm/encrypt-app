from encryption.encryption_base import Encryption
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


    def encrypt_input(self, userInput):
        shift = self.get_shift_value()
        self.encryptedContent = list(userInput)

        if shift == "":
            shift = random.randint(0, 1024)
            logger.info(f"User chose shift of {shift} ")
        else: 
            logger.info(f"User chose shift of {shift}")
        for pos in range(len(userInput)):
            if userInput[pos] == " ":
                self.encryptedContent[pos] = " "
            elif userInput[pos] == "~":
                self.encryptedContent[pos] = self.alphabet[0]
            else:
                y = self.alphabet.index(userInput[pos])
                
                if y + shift > len(self.alphabet): 
                    rest = shift % len(self.alphabet)
                    difference = len(self.alphabet) - y
                    rest = rest - difference
                    self.encryptedContent[pos] = self.alphabet[rest]
                else: 
                    self.encryptedContent[pos] = self.alphabet[y+shift]

        self.encryptedContent = "".join(self.encryptedContent)

