import unittest
from models import EncryptionBase
from unittest.mock import patch


class TestCaesarEncryption(unittest.TestCase):

    def setUp(self):
        self.mock_encryption = EncryptionBase()

    @patch('builtins.input', lambda *args: "ab cd    ")
    def test_should_return_ab_cd_given_input_ab_cd(self):
        self.assertEqual(self.mock_encryption.get_user_input_from_cli(), "ab cd    ")

    def test_should_raise_Exception_given_input_with_special_characters(self):
        with self.assertRaises(ValueError):
            self.mock_encryption.validate_input("äöü")


if __name__ == '__main__':
    unittest.main()