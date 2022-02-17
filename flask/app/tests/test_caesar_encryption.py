import unittest
from unittest.mock import patch
from flask.app.model.models import CaesarEncryption


class TestCaesarEncryption(unittest.TestCase):

    def setUp(self):
        self.mock_encryption = CaesarEncryption()

    @patch('builtins.input', lambda *args: "1")
    def test_should_return_bcd_given_input_abc(self):
        shift = int(input())
        encrypted_string = self.mock_encryption.encrypt_input("abc", shift)
        self.assertEqual(encrypted_string, "bcd")

    @patch('builtins.input', lambda *args: "1")
    def test_should_return_bc_d_given_input_ab_c(self):
        shift = int(input())
        encrypted_string = self.mock_encryption.encrypt_input("ab c", shift)
        self.assertEqual(encrypted_string, "bc d")

    @patch('builtins.input', lambda *args: "1")
    def test_should_return_excl_given_input_9(self):
        shift = int(input())
        encrypted_string = self.mock_encryption.encrypt_input("9", shift)
        self.assertEqual(encrypted_string, "!")

    @patch('builtins.input', lambda *args: "1")
    def test_should_return_excl_bcd_given_input_9abc(self):
        shift = int(input())
        encrypted_string = self.mock_encryption.encrypt_input("9abc", shift)
        self.assertEqual(encrypted_string, "!bcd")

    @patch('builtins.input', lambda *args: "1")
    def test_should_return_a_given_input_tilde(self):
        shift = int(input())
        encrypted_string = self.mock_encryption.encrypt_input("~", shift)
        self.assertEqual(encrypted_string, "a")

    @patch('builtins.input', lambda *args: "1")
    def test_should_return_quotes_given_input_excl(self):
        shift = int(input())
        encrypted_string = self.mock_encryption.encrypt_input("!", shift)
        self.assertEqual(encrypted_string, "\"")

    @patch('builtins.input', lambda *args: "2")
    def test_should_return_c_given_input_a(self):
        shift = int(input())
        encrypted_string = self.mock_encryption.encrypt_input("a", shift)
        self.assertEqual(encrypted_string, "c")

    @patch('builtins.input', lambda *args: "26")
    def test_should_return_A_given_input_a(self):
        shift = int(input())
        encrypted_string = self.mock_encryption.encrypt_input("a", shift)
        self.assertEqual(encrypted_string, "A")


if __name__ == '__main__':
    unittest.main()
