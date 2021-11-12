from encryption.encryption_base import Encryption
import random

class CaesarEncryption(Encryption):
    
    def encrypt_input(self, userInput, shift = ""):
        self.encryptedContent = list(userInput)

        if shift == "":
            shift = random.randint(0, 1024)
        else: 
            shift = int(shift)

        for pos in range(len(userInput)):
            if userInput[pos] == " ":
                self.encryptedContent[pos] = " "
            elif userInput[pos] == "~":
                self.encryptedContent[pos] = self.alphabet[0]
            else:
                y = self.alphabet.index(userInput[pos])
                
                if y + shift > len(self.alphabet): 
                    rest = shift % len(self.alphabet)
                    differenz = len(self.alphabet) - y
                    rest = rest - differenz
                    self.encryptedContent[pos] = self.alphabet[rest]
                else: 
                    self.encryptedContent[pos] = self.alphabet[y+shift]

        self.encryptedContent = "".join(self.encryptedContent)