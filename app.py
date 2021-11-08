from encryption.caesar_encryption import CaesarEncryption
from encryption.monoalphabetic_substitution import MonoalphabeticSubstitution


class App:

    if __name__ == '__main__':
        encryptionType = input("Press c for Caesar Encryption and m for Monoalphabetic Substitution: ")

        if encryptionType == "c":
            print("Caeser Encryption started. Please enter a word to encrypt: ")
            while True: 
                newEncryption = CaesarEncryption()
                newEncryption.get_userInput_from_cli()
                newEncryption.encrypt_input(newEncryption.userInput)
                print(newEncryption.encryptedContent)
        
        if encryptionType == "m":
            print("Monoalphabetic Substitution Encryption started. Please enter a word to encrypt: ")
            while True: 
                newEncryption = MonoalphabeticSubstitution()
                newEncryption.get_userInput_from_cli()
                newEncryption.encrypt_input(newEncryption.userInput)
                print(newEncryption.encryptedContent)
        
        
            
    