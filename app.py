class Encryption:

    def __init__(self):
        self.alphabetIndex = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
            "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
            "0","1","2","3","4","5","6","7","8","9"]
    

    def get_userInput_from_cli(self):
        newInput = input()
        self.userInput = newInput


    def encrypt_input(self, userInput):
        #TODO @ Lina :), currently encryptedInput is a placeholder variable
    
        encryptedInput = userInput + "-encrypted"
        self.encryptedContent = encryptedInput

        
class CaesarEncryption(Encryption):
    pass



####Tests below here###
def test_1_encrypt_input():
    sampleInput = "sampleInputHere"
    expected = "sampleInputHere-encrypted"
    sampleEncryption = CaesarEncryption()
    sampleEncryption.encrypt_input(sampleInput)
    result = sampleEncryption.encryptedContent

    if expected != result:
        raise Exception("test failed")


def test_2_encrypt_input():
    sampleInput = "blareghoiawgnlanwe-1335-$=/)$§`'*"
    expected = "blareghoiawgnlanwe-1335-$=/)$§`'*-encrypted"
    sampleEncryption = CaesarEncryption()
    sampleEncryption.encrypt_input(sampleInput)
    result = sampleEncryption.encryptedContent

    if expected != result:
        raise Exception("test failed")
        


def runTests():
    
    test_1_encrypt_input()
    test_2_encrypt_input()


def main():
    while True: 
        newEncryption = CaesarEncryption()
        newEncryption.get_userInput_from_cli()
        newEncryption.encrypt_input(newEncryption.userInput)
        print(newEncryption.encryptedContent)


runTests()
main()