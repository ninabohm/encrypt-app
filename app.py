from flask import Flask, redirect, url_for, render_template
import logging, sys
from encryption.caesar_encryption import CaesarEncryption
from encryption.monoalphabetic_substitution import MonoalphabeticSubstitution
from menu.menu import Menu

app = Flask(__name__)

logging.basicConfig(stream=sys.stdout,
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    #app.run()
    promptMenu = Menu()
    promptMenu.print_menu()

    while True:
        value = input("Choose a value and press Enter: ")

        if value == "1":
            logging.info("Caesar Encryption started")
            while True:
                newEncryption = CaesarEncryption()
                print("Please insert a string")
                newEncryption.get_userInput_from_cli()
                shift = input("Please insert the offset/vector (Press Enter for a random value): ")
                newEncryption.encrypt_input(newEncryption.userInput, shift)
                print(newEncryption.encryptedContent)

        if value == "2":
            logging.info("Monoalphabetic Substitution Encryption started")
            while True:
                newEncryption = MonoalphabeticSubstitution()
                newEncryption.get_userInput_from_cli()
                newEncryption.encrypt_input(newEncryption.userInput)
                print(newEncryption.encryptedContent)

        if value == "3":
            print("Welcome to the amazing encrypt-app made by the **X-inas**.")

        if value == "4":
            exit()


    
