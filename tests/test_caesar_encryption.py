import unittest
from unittest.mock import patch
from encryption.caesar_encryption import CaesarEncryption


class TestCaesarEncryption(unittest.TestCase):

        def setUp(self):
                self.mock_encryption = CaesarEncryption()


        @patch('builtins.input', lambda *args: "1")
        def test_should_return_bcd_given_input_abc(self):
                self.mock_encryption.encrypt_input("abc")
                self.assertEqual(self.mock_encryption.encryptedContent, "bcd")


        @patch('builtins.input', lambda *args: "1")
        def test_should_return_bc_d_given_input_ab_c(self):
                self.mock_encryption.encrypt_input("ab c")
                self.assertEqual(self.mock_encryption.encryptedContent, "bc d")


        @patch('builtins.input', lambda *args: "1")
        def test_should_return_excl_given_input_9(self):
                self.mock_encryption.encrypt_input("9")
                self.assertEqual(self.mock_encryption.encryptedContent, "!")


        @patch('builtins.input', lambda *args: "1")
        def test_should_return_excl_bcd_given_input_9abc(self):
                self.mock_encryption.encrypt_input("9abc")
                self.assertEqual(self.mock_encryption.encryptedContent, "!bcd")


        @patch('builtins.input', lambda *args: "1")
        def test_should_return_a_given_input_tilde(self):
                self.mock_encryption.encrypt_input("~")
                self.assertEqual(self.mock_encryption.encryptedContent, "a")


        @patch('builtins.input', lambda *args: "1")
        def test_should_return_quotes_given_input_excl(self):
                self.mock_encryption.encrypt_input("!")
                self.assertEqual(self.mock_encryption.encryptedContent, "\"")


        @patch('builtins.input', lambda *args: "2")
        def test_should_return_c_given_input_a(self):
                self.mock_encryption.encrypt_input("a")
                self.assertEqual(self.mock_encryption.encryptedContent, "c")


        @patch('builtins.input', lambda *args: "26")
        def test_should_return_A_given_input_a(self):
                self.mock_encryption.encrypt_input("a")
                self.assertEqual(self.mock_encryption.encryptedContent, "A")



if __name__ == '__main__':
    unittest.main()