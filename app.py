from encryption.caesar_encryption import CaesarEncryption
from encryption.monoalphabetic_substitution import MonoalphabeticSubstitution


if __name__ == '__main__':
    print("chosse \"c\" for Caesar Encryption and \"m\" for Monoalphabetic Substitution")
    encryptionType = input()
    if encryptionType == "c":
        while True: 
            newEncryption = CaesarEncryption()
            newEncryption.get_userInput_from_cli()
            newEncryption.encrypt_input(newEncryption.userInput)
            print(newEncryption.encryptedContent)
    
    if encryptionType == "m":
        while True: 
            newEncryption = MonoalphabeticSubstitution()
            newEncryption.get_userInput_from_cli()
            newEncryption.encrypt_input(newEncryption.userInput)
            print(newEncryption.encryptedContent)
    