import unittest
from unittest.mock import patch
from encryption.caesar_encryption import CaesarEncryption
from app import InvalidInputException


class TestCeasarEncryption(unittest.TestCase):

        def setUp(self):
                self.mock_encryption = CaesarEncryption()


        @patch('builtins.input', lambda *args: "lasse")
        def test_should_return_lasse_given_input_lasse(self):
                self.assertEqual(self.mock_encryption.get_userInput_from_cli(), "lasse")


        @patch('builtins.input', lambda *args: "ab cd    ")
        def test_should_return_ab_cd_given_input_ab_cd(self):
                self.assertEqual(self.mock_encryption.get_userInput_from_cli(), "ab cd    ")


        @patch('builtins.input', lambda *args: "abc√√√√√")
        def test_should_throw_InvalidInputException_given_input_with_characters_not_in_list(self):
                with self.assertRaises(ValueError): self.mock_encryption.get_userInput_from_cli()


        def test_should_return_True_given_input_asdf(self):
                self.assertTrue(self.mock_encryption.validate_input("asdf"))


        def test_should_return_True_given_input_with_special_charcters(self):
                self.assertTrue(self.mock_encryption.validate_input("asdf&&&&"))


        def test_should_return_bcd_given_input_abc(self):
                self.mock_encryption.encrypt_input("abc")
                self.assertEqual(self.mock_encryption.encryptedContent, "bcd")


        def test_should_return_bc_d_given_input_ab_c(self):
                self.mock_encryption.encrypt_input("ab c")
                self.assertEqual(self.mock_encryption.encryptedContent, "bc d")


        def test_should_return_excl_given_input_9(self):
                self.mock_encryption.encrypt_input("9")
                self.assertEqual(self.mock_encryption.encryptedContent, "!")
                

        def test_should_return_excl_bcd_given_input_9abc(self):
                self.mock_encryption.encrypt_input("9abc")
                self.assertEqual(self.mock_encryption.encryptedContent, "!bcd")


        def test_should_return_a_given_input_tilde(self):
                self.mock_encryption.encrypt_input("~")
                self.assertEqual(self.mock_encryption.encryptedContent, "a")
        

        def test_should_return_quotes_given_input_excl(self):
                self.mock_encryption.encrypt_input("!")
                self.assertEqual(self.mock_encryption.encryptedContent, "\"")


if __name__ == '__main__':
    unittest.main()