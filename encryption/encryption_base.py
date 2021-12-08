import logging
import string


logger = logging.getLogger(__name__)


class Encryption:
    
    def __init__(self):
        self.alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        self.shift = ""
        self.user_input = ""

    def get_user_input_from_cli(self):
        self.user_input = input()
        try:
            self.validate_input(self.user_input)
        except ValueError as error:
            logger.info(error)
            self.get_user_input_from_cli()
        return self.user_input

    def validate_input(self, user_input):
        for char in user_input:
            if char not in self.alphabet and char != " ":
                raise ValueError("Sorry, only no special characters allowed. Please try again.")
