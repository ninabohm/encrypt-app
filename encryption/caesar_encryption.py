from encryption.encryption_base import Encryption
import random

class CaesarEncryption(Encryption):
    
    def encrypt_input(self, userInput, shift = 0):
        self.encryptedContent = list(userInput)

        if shift == 0:
            shift = random.randint(0, 1024)

        for pos in range(len(userInput)):
            if userInput[pos] == " ":
                self.encryptedContent[pos] = " "
            elif userInput[pos] == "~":
                self.encryptedContent[pos] = self.alphabet[0]
            else:
                y = self.alphabet.index(userInput[pos])
                self.encryptedContent[pos] = self.alphabet[y+shift]
        self.encryptedContent = "".join(self.encryptedContent)