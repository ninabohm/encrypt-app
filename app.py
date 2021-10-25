class UserInput:

    def __init__(self, content):
        self.content = content



class Encryption:

    def __init__(self):
        self.alphabetIndex = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
            "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
            "0","1","2","3","4","5","6","7","8","9"]
        self.encryptedContent = ""
        

    def encrypt_input(self, userInput):
        #TODO @ Lina :), currently encryptedInput is a placeholder variable
        
        encryptedInput = userInput + "-encrypted"
        self.encryptedContent = encryptedInput


class CaesarEncryption(Encryption):
    pass


# sampleEncryption = CaesarEncryption()

# sampleEncryption.encrypt_input("kevino")
# print(sampleEncryption.encryptedContent)


####Tests below here###
def test1_init_UserInput():
    sampleInput = "foobar"
    expected = "foobar"
    newInput = UserInput(sampleInput)
    result = newInput.content

    if expected != result:
        raise Exception("test failed")


def test2_init_UserInput():
    sampleInput = "bla bla12  35//)(!?***"
    expected = "bla bla12  35//)(!?***"
    newInput = UserInput(sampleInput)
    result = newInput.content

    if expected != result:
        raise Exception("test failed")


def test1_encrypt_input():
    sampleInput = "sampleInputHere"
    expected = "sampleInputHere-encrypted"
    sampleEncryption = CaesarEncryption()
    sampleEncryption.encrypt_input(sampleInput)
    result = sampleEncryption.encryptedContent

    if expected != result:
        raise Exception("test failed")


def test2_encrypt_input():
    sampleInput = "blareghoiawgnlanwe-1335-$=/)$§`'*"
    expected = "blareghoiawgnlanwe-1335-$=/)$§`'*-encrypted"
    sampleEncryption = CaesarEncryption()
    sampleEncryption.encrypt_input(sampleInput)
    result = sampleEncryption.encryptedContent

    if expected != result:
        raise Exception("test failed")
        


def runTests():
    test1_init_UserInput()
    test2_init_UserInput()
    test1_encrypt_input()
    test2_encrypt_input()


runTests()

#get_user_input()