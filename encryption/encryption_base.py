import logging
import string

logger = logging.getLogger(__name__)

class Encryption:
    
    def __init__(self):
        self.alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation


    def get_userInput_from_cli(self):
        self.userInput = input()
        try:
            self.validate_input(self.userInput)
        except ValueError as error:
            logger.info(error)
            self.get_userInput_from_cli()
        return self.userInput


    def validate_input(self, userInput):
        for char in userInput:
            if char not in self.alphabet and char != " ":
                   raise ValueError("Sorry, only no special characters allowed. Please try again.")
