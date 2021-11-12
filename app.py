import logging, sys
from encryption.caesar_encryption import CaesarEncryption
from encryption.monoalphabetic_substitution import MonoalphabeticSubstitution


class App:

    logging.basicConfig(stream=sys.stdout, 
    encoding="utf-8", 
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

    if __name__ == '__main__':
        encryptionType = input("Press c for Caesar Encryption and m for Monoalphabetic Substitution: ")

        if encryptionType == "c":
            logging.info("Caeser Encryption started")
            while True: 
                newEncryption = CaesarEncryption()
                newEncryption.get_userInput_from_cli()
                newEncryption.encrypt_input(newEncryption.userInput)
                print(newEncryption.encryptedContent)
        
        if encryptionType == "m":
            logging.info("Monoalphabetic Substitution Encryption started")
            while True: 
                newEncryption = MonoalphabeticSubstitution()
                newEncryption.get_userInput_from_cli()
                newEncryption.encrypt_input(newEncryption.userInput)
                print(newEncryption.encryptedContent)
        
        
            
    
