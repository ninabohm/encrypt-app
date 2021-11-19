class Menu:

    def print_menu(self):
        print("1: Caesar Encryption")
        print("2: Monoalphabetic Substitution Encryption")
        print("3: About")
        print("4: Quit program")


    def get_user_action(self):
        self.value = input("Choose a value and press Enter: ")

