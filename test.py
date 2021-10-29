def get_userInput_from_cli(self):
        newInput = input()
        self.userInput = newInput


def encrypt_input(self, userInput):
        #TODO @ Lina :), currently encryptedInput is a placeholder variable

        caeserencryption = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
            "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
            "0","1","2","3","4","5","6","7","8","9"]

        def caeserencryption (userInput):
            for x in userInput:
                if x == " ":
                    userInput[x] = " "
                elif x == "9":
                    userInput[x] = caeserencryption[0]
                else:
                    y = caeserencryption.index(userInput[x])
                    userInput[x] = caeserencryption[y+1]
        
        encryptedInput = userInput + "-encrypted"
        self.encryptedContent = encryptedInput