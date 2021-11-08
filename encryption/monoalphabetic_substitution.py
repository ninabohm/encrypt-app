from encryption.encryption_base import Encryption

class MonoalphabeticSubstitution(Encryption):

    def encrypt_input(self, userInput):
        self.encryptedContent = list(userInput)
        for pos in range(len(userInput)):
            if userInput[pos] == " ":
                self.encryptedContent[pos] = " "
            else: 
                left = self.alphabet.index(userInput[pos])
                right = len(self.alphabet) - 1 - left
                self.encryptedContent[pos] = self.alphabet[right]
        self.encryptedContent = "".join(self.encryptedContent)