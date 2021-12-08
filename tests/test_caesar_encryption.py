import unittest
from unittest.mock import patch
from encryption.caesar_encryption import CaesarEncryption
from encryption.encrypted_string import EncryptedString


class TestCaesarEncryption(unittest.TestCase):

    def setUp(self):
        self.mock_encryption = CaesarEncryption()

    @patch('builtins.input', lambda *args: "1")
    def test_should_return_bcd_given_input_abc(self):
        encrypted_string = self.mock_encryption.encrypt_input("abc")
        self.assertEqual(encrypted_string, "bcd")

    @patch('builtins.input', lambda *args: "1")
    def test_should_return_bc_d_given_input_ab_c(self):
        encrypted_string = self.mock_encryption.encrypt_input("ab c")
        self.assertEqual(encrypted_string, "bc d")

    @patch('builtins.input', lambda *args: "1")
    def test_should_return_excl_given_input_9(self):
        encrypted_string = self.mock_encryption.encrypt_input("9")
        self.assertEqual(encrypted_string, "!")

    @patch('builtins.input', lambda *args: "1")
    def test_should_return_excl_bcd_given_input_9abc(self):
        encrypted_string = self.mock_encryption.encrypt_input("9abc")
        self.assertEqual(encrypted_string, "!bcd")

    @patch('builtins.input', lambda *args: "1")
    def test_should_return_a_given_input_tilde(self):
        encrypted_string = self.mock_encryption.encrypt_input("~")
        self.assertEqual(encrypted_string, "a")

    @patch('builtins.input', lambda *args: "1")
    def test_should_return_quotes_given_input_excl(self):
        encrypted_string = self.mock_encryption.encrypt_input("!")
        self.assertEqual(encrypted_string, "\"")

    @patch('builtins.input', lambda *args: "2")
    def test_should_return_c_given_input_a(self):
        encrypted_string = self.mock_encryption.encrypt_input("a")
        self.assertEqual(encrypted_string, "c")

    @patch('builtins.input', lambda *args: "26")
    def test_should_return_A_given_input_a(self):
        encrypted_string = self.mock_encryption.encrypt_input("a")
        self.assertEqual(encrypted_string, "A")



if __name__ == '__main__':
    unittest.main()
