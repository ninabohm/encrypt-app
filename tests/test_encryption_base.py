import unittest
from unittest.mock import patch
from encryption.encryption_base import Encryption


class TestEncryption(unittest.TestCase):

        def setUp(self):
            self.mock_encryption = Encryption()


        @patch('builtins.input', lambda *args: "lasse")
        def test_should_return_lasse_given_input_lasse(self):
            self.assertEqual(self.mock_encryption.get_user_input_from_cli(), "lasse")


        @patch('builtins.input', lambda *args: "ab cd    ")
        def test_should_return_ab_cd_given_input_ab_cd(self):
            self.assertEqual(self.mock_encryption.get_user_input_from_cli(), "ab cd    ")


        def test_should_raise_Exception_given_input_with_special_characters(self):
            with self.assertRaises(ValueError): self.mock_encryption.validate_input("äöü")


if __name__ == '__main__':
    unittest.main()