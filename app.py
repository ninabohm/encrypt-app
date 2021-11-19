from flask import Flask, redirect, url_for, render_template
import logging, sys
from encryption.caesar_encryption import CaesarEncryption
from encryption.monoalphabetic_substitution import MonoalphabeticSubstitution
from menu.menu import Menu


logging.basicConfig(stream=sys.stdout,
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")



if __name__ == "__main__":
    menu = Menu()

    encryption = menu.define_encryption_type()
    print("Please insert a string")
    encryption.get_userInput_from_cli()
    shift = input("Please insert the offset/vector (Press Enter for a random value): ")
    encryption.encrypt_input(encryption.userInput, shift)
    print(encryption.encryptedContent)


    if menu.option == "2":
        logging.info("Monoalphabetic Substitution Encryption started")
        while True:
            encryption = MonoalphabeticSubstitution()
            print("Please insert a string")
            encryption.get_userInput_from_cli()
            encryption.encrypt_input(encryption.userInput)
            print(encryption.encryptedContent)

    if menu.option == "3":
        print("Welcome to the encrypt-app")

    if menu.option == "4":
        exit()


    
