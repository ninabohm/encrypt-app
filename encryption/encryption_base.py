import string

class Encryption:
    
    def __init__(self):
        self.alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        #for reference: alphabet contains the following values: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    def get_userInput_from_cli(self):
        self.userInput = input()
        if not self.validate_input(self.userInput):
            raise ValueError("Please only use words without special characters")
        return self.userInput


    def validate_input(self, userInput):
        for char in userInput:
            if char not in self.alphabet and char != " ":
                    return False 
        return True