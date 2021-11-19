from user.user_list import user_list
import logging


logger = logging.getLogger(__name__)

class User:

    def __init__(self):
        self.logged_in = False


    def create_user(self):
        self.firstName = input("Please type your first name and press enter ")


    def save_user(self):
        user_list.append(self.firstName)
        logger.info(f"User with first name {self.firstName} saved in user list")


    def check_if_in_user_list(self, user):
        return user in user_list

