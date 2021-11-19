from encryption.caesar_encryption import CaesarEncryption
from encryption.monoalphabetic_substitution import MonoalphabeticSubstitution

class Menu:

    def __init__(self):
        self.print_menu()
        self.option = input("Choose a value and press Enter: ")


    def print_menu(self):
        print("1: Caesar Encryption")
        print("2: Monoalphabetic Substitution Encryption")
        print("3: About")
        print("4: Quit program")


    def define_encryption_type_or_exit(self):
        if self.option == "1":
            return CaesarEncryption()

        if self.option == "2":
            return MonoalphabeticSubstitution()

        if self.option == "3":
            print("Welcome to the encrypt-app")

        if self.option == "4":
            exit()