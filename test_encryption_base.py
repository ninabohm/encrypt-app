import unittest
from unittest.mock import patch
from encryption.encryption_base import Encryption


class TestEncryption(unittest.TestCase):

        def setUp(self):
                self.mock_encryption = Encryption()


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



if __name__ == '__main__':
    unittest.main()