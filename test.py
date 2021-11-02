
userInput = "abcd"

def encrypt_input(userInput):
        #TODO @ Lina :), currently encryptedInput is a placeholder variable

        alphabetIndex = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
            "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
            "0","1","2","3","4","5","6","7","8","9"]

        for x in range(len(userInput)):
            if x == " ":
                userInput[x] = " "
            elif x == "9":
                userInput[x] = alphabetIndex[0]
            else:
                y = alphabetIndex.index(userInput[x])
                userInput[x] = alphabetIndex[y+1]
        
        #encryptedInput = userInput + "-encrypted"
        #self.encryptedContent = encryptedInput


encrypt_input(userInput)
