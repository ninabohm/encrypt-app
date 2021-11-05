class Encryption:
    
    def __init__(self):
        self.alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
            "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
            "0","1","2","3","4","5","6","7","8","9"]
    

    def get_userInput_from_cli(self):
        self.userInput = input()
        return self.userInput 


    def encrypt_input(self, userInput):
        if not self.validate_input(userInput):
            raise InvalidInputException("Please only use words without special characters")

        workingInput = list(userInput)
        for pos in range(len(userInput)):
            if userInput[pos] == " ":
                workingInput[pos] = " "
            elif userInput[pos] == "9":
                workingInput[pos] = self.alphabet[0]
            else:
                y = self.alphabet.index(userInput[pos])
                workingInput[pos] = self.alphabet[y+1]
        
        self.encryptedContent = "".join(workingInput)


    def validate_input(self, userInput):
        for char in userInput:
            if char not in self.alphabet and char != " ":
                    return False
                
        return True  

        
class CaesarEncryption(Encryption):
    pass



class InvalidInputException(Exception):
    pass


if __name__ == '__main__':
    while True: 
        newEncryption = CaesarEncryption()
        newEncryption.get_userInput_from_cli()
        newEncryption.encrypt_input(newEncryption.userInput)
        print(newEncryption.encryptedContent)

