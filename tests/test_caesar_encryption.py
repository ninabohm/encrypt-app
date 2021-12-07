import unittest
from unittest.mock import patch
from encryption.caesar_encryption import CaesarEncryption
from encryption.encrypted_string import EncryptedString


class TestCaesarEncryption(unittest.TestCase):

        def setUp(self):
                self.mock_encryption = CaesarEncryption()


        @patch('builtins.input', lambda *args: "1")
        def test_should_return_bcd_given_input_abc(self):
                self.mock_encryption.encrypt_input("abc")
                self.assertEqual(self.mock_encryption.encrypted_string, "bcd")


        @patch('builtins.input', lambda *args: "1")
        def test_should_return_bc_d_given_input_ab_c(self):
                self.mock_encryption.encrypt_input("ab c")
                self.assertEqual(self.mock_encryption.encrypted_string, "bc d")


        @patch('builtins.input', lambda *args: "1")
        def test_should_return_excl_given_input_9(self):
                self.mock_encryption.encrypt_input("9")
                self.assertEqual(self.mock_encryption.encrypted_string, "!")


        @patch('builtins.input', lambda *args: "1")
        def test_should_return_excl_bcd_given_input_9abc(self):
                self.mock_encryption.encrypt_input("9abc")
                self.assertEqual(self.mock_encryption.encrypted_string, "!bcd")


        @patch('builtins.input', lambda *args: "1")
        def test_should_return_a_given_input_tilde(self):
                self.mock_encryption.encrypt_input("~")
                self.assertEqual(self.mock_encryption.encrypted_string, "a")


        @patch('builtins.input', lambda *args: "1")
        def test_should_return_quotes_given_input_excl(self):
                self.mock_encryption.encrypt_input("!")
                self.assertEqual(self.mock_encryption.encrypted_string, "\"")


        @patch('builtins.input', lambda *args: "2")
        def test_should_return_c_given_input_a(self):
                self.mock_encryption.encrypt_input("a")
                self.assertEqual(self.mock_encryption.encrypted_string, "c")


        @patch('builtins.input', lambda *args: "26")
        def test_should_return_A_given_input_a(self):
                self.mock_encryption.encrypt_input("a")
                self.assertEqual(self.mock_encryption.encrypted_string, "A")


        @patch('builtins.input', lambda *args: "1")
        def test_should_return_encrypted_string_as_type(self):
                sample_encryption = self.mock_encryption.encrypt_input("abc")
                self.assertIsInstance(sample_encryption, EncryptedString)


if __name__ == '__main__':
    unittest.main()