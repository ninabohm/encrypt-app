from encryption.encryption_base import Encryption


class CaesarEncryption(Encryption):
    
    def encrypt_input(self, userInput):
        self.encryptedContent = list(userInput)
        for pos in range(len(userInput)):
            if userInput[pos] == " ":
                self.encryptedContent[pos] = " "
            elif userInput[pos] == "~":
                self.encryptedContent[pos] = self.alphabet[0]
            else:
                y = self.alphabet.index(userInput[pos])
                self.encryptedContent[pos] = self.alphabet[y+1]
        self.encryptedContent = "".join(self.encryptedContent)