class Encryption:
    
    def __init__(self):
        self.alphabetIndex = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
            "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
            "0","1","2","3","4","5","6","7","8","9"]
    

    def get_userInput_from_cli(self):
        self.userInput = input()
        return self.userInput 


    def encrypt_input(self, userInput):
        #TODO @ Lina :), currently encryptedInput is a placeholder variable

        for x in range(len(userInput)):
            if x == " ":
                userInput[x] = " "
            elif x == "9":
                userInput[x] = self.alphabetIndex[0]
            else:
                y = self.alphabetIndex.index(userInput[x])
                userInput[x] = self.alphabetIndex[y+1]
        
        encryptedInput = userInput + "-encrypted"
        self.encryptedContent = encryptedInput

        
class CaesarEncryption(Encryption):

    pass

def main():
    while True:         
        newEncryption = CaesarEncryption()
        newEncryption.get_userInput_from_cli()
        newEncryption.encrypt_input(newEncryption.userInput, 2)
        print(newEncryption.encryptedContent)


