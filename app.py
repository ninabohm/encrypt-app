from flask import Flask, redirect, url_for, render_template
import logging, sys
from menu.menu import Menu


logging.basicConfig(stream=sys.stdout,
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

class App:

    def __init__(self):
        self.menu = Menu()

    def keep_encryption_alive(self):
        while True:
            encryption = self.menu.define_encryption_type_or_exit()
            print("Please insert a string")
            encryption.get_userInput_from_cli()
            encryption.encrypt_input(encryption.userInput)
            print(encryption.encryptedContent)


    def login(self):
        return 0


if __name__ == "__main__":
    app = App()
    app.login()
    app.keep_encryption_alive()






    
