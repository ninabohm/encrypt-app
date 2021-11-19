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
    menu.print_menu()
    menu.get_user_action()

    while True:
        if menu.value == "1":
            logging.info("Caesar Encryption started")
            while True:
                newEncryption = CaesarEncryption()
                print("Please insert a string")
                newEncryption.get_userInput_from_cli()
                shift = input("Please insert the offset/vector (Press Enter for a random value): ")
                newEncryption.encrypt_input(newEncryption.userInput, shift)
                print(newEncryption.encryptedContent)

        if menu.value == "2":
            logging.info("Monoalphabetic Substitution Encryption started")
            while True:
                newEncryption = MonoalphabeticSubstitution()
                newEncryption.get_userInput_from_cli()
                newEncryption.encrypt_input(newEncryption.userInput)
                print(newEncryption.encryptedContent)

        if menu.value == "3":
            print("Welcome to the encrypt-app")

        if menu.value == "4":
            exit()


    
