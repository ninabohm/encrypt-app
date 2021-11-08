import unittest
from unittest.mock import patch
from app import CaesarEncryption
from app import InvalidInputException


class TestApp(unittest.TestCase):

        def setUp(self):
                self.mock_encryption = CaesarEncryption()


        @patch('builtins.input', lambda *args: "lasse")
        def test_should_return_lasse_given_input_lasse(self):
                self.assertEqual(self.mock_encryption.get_userInput_from_cli(), "lasse")


        # @patch('builtins.input', lambda *args: "sampleInputHere13498715389(/&$%/&")
        # def test_should_return_input_with_special_characters(self):
        #         self.assertEqual(self.mock_encryption.get_userInput_from_cli(), "sampleInputHere13498715389(/&$%/&")


        @patch('builtins.input', lambda *args: "ab cd    ")
        def test_should_return_ab_cd_given_input_ab_cd(self):
                self.assertEqual(self.mock_encryption.get_userInput_from_cli(), "ab cd    ")


        def test_should_return_bcd_given_input_abc(self):
                self.mock_encryption.encrypt_input("abc")
                self.assertEqual(self.mock_encryption.encryptedContent, "bcd")


        def test_should_return_bc_d_given_input_ab_c(self):
                self.mock_encryption.encrypt_input("ab c")
                self.assertEqual(self.mock_encryption.encryptedContent, "bc d")


        def test_should_return_a_given_input_9(self):
                self.mock_encryption.encrypt_input("9")
                self.assertEqual(self.mock_encryption.encryptedContent, "a")
                

        def test_should_return_abcd_given_input_9abc(self):
                self.mock_encryption.encrypt_input("9abc")
                self.assertEqual(self.mock_encryption.encryptedContent, "abcd")


        def test_should_return_True_given_input_asdf(self):
                self.assertTrue(self.mock_encryption.validate_input("asdf"))


        def test_should_return_False_given_input_with_special_charcters(self):
                self.assertFalse(self.mock_encryption.validate_input("asdf&&&&"))


        @patch('builtins.input', lambda *args: "abc&&//!!")
        def test_should_throw_InvalidInputException_given_input_with_special_characters(self):
                with self.assertRaises(InvalidInputException): self.mock_encryption.get_userInput_from_cli()



if __name__ == '__main__':
    unittest.main()