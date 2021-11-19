from flask import Flask, redirect, url_for, render_template
import logging, sys
from menu.menu import Menu
from user.user import User


logging.basicConfig(stream=sys.stdout,
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")


class App:

    def start(self):
        logging.info("Application up and running")
        option = input("Please press 1 to login or 2 to register ")
        if option == "1":
            self.login()

        if option == "2":
            self.register()


    def login(self):
        logging.info("Login started")


    def register(self):
        logging.info("Registering started")
        user = User()
        return user


    def create_menu(self):
        self.menu = Menu()


    def keep_encryption_alive(self):
        while True:
            encryption = self.menu.define_encryption_type_or_exit()
            print("Please insert a string ")
            encryption.get_userInput_from_cli()
            encryption.encrypt_input(encryption.userInput)
            print(encryption.encryptedContent)


if __name__ == "__main__":
    app = App()
    app.start()
    app.create_menu()
    app.keep_encryption_alive()






    
