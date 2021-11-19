from encryption.caesar_encryption import CaesarEncryption

class Menu:

    def __init__(self):
        self.print_menu()
        self.option = input("Choose a value and press Enter: ")


    def print_menu(self):
        print("1: Caesar Encryption")
        print("2: Monoalphabetic Substitution Encryption")
        print("3: About")
        print("4: Quit program")


    def define_encryption_type(self):
        if self.option == "1":
            return CaesarEncryption()
