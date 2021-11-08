class Encryption:
    
    def __init__(self):
        self.alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
            "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
            "0","1","2","3","4","5","6","7","8","9",
            "!","\"","#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","\\","]","^","_","`","{","|","}","~"]
    

    def get_userInput_from_cli(self):
        self.userInput = input()
        if not self.validate_input(self.userInput):
            raise ValueError("Please only use words without special characters")
        return self.userInput


    def validate_input(self, userInput):
        for char in userInput:
            if char not in self.alphabet and char != " ":
                    return False
                
        return True