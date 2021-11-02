import unittest
from unittest.mock import patch
from app import CaesarEncryption
from app import InvalidInputException


class TestGetUserInput(unittest.TestCase):

    def setUp(self):
        self.mock_encryption = CaesarEncryption()

    @patch('builtins.input', lambda *args: "lasse")
    def test_should_return_input(self):
            self.assertEqual(self.mock_encryption.get_userInput_from_cli(), "lasse")


    @patch('builtins.input', lambda *args: "sampleInputHere13498715389(/&$%/&")
    def test_should_return_input_with_special_characters(self):
            self.assertEqual(self.mock_encryption.get_userInput_from_cli(), "sampleInputHere13498715389(/&$%/&")



class TestEncryptInput(unittest.TestCase):

    def setUp(self):
        self.mock_encryption = CaesarEncryption()  

    def test_should_return_bcd_given_input_abc(self):
        self.mock_encryption.encrypt_input("abc")
        self.assertEqual(self.mock_encryption.encryptedContent, "bcd")

    
    def test_should_return_True_given_input_asdf(self):
        self.assertTrue(self.mock_encryption.validate_input("asdf"))

    
    def test_should_return_False_given_input_with_special_charcters(self):
        self.assertFalse(self.mock_encryption.validate_input("asdf&&&&"))

    
    def test_should_throw_InvalidInputException_given_input_with_special_characters(self):
        with self.assertRaises(InvalidInputException): self.mock_encryption.encrypt_input("abc&&//!!")



if __name__ == '__main__':
    unittest.main()