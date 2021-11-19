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


def keep_encryption_alive():
    while True:
        encryption = menu.define_encryption_type_or_exit()
        print("Please insert a string")
        encryption.get_userInput_from_cli()
        encryption.encrypt_input(encryption.userInput)
        print(encryption.encryptedContent)


if __name__ == "__main__":
    menu = Menu()
    keep_encryption_alive()






    
