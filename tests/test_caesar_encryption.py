import unittest
from unittest.mock import patch
from encryption.caesar_encryption import CaesarEncryption


class TestCaesarEncryption(unittest.TestCase):

        def setUp(self):
                self.mock_encryption = CaesarEncryption()


        def test_should_return_bcd_given_input_abc(self):
                self.mock_encryption.encrypt_input("abc", 1)
                self.assertEqual(self.mock_encryption.encryptedContent, "bcd")


        def test_should_return_bc_d_given_input_ab_c(self):
                self.mock_encryption.encrypt_input("ab c", 1)
                self.assertEqual(self.mock_encryption.encryptedContent, "bc d")


        def test_should_return_excl_given_input_9(self):
                self.mock_encryption.encrypt_input("9", 1)
                self.assertEqual(self.mock_encryption.encryptedContent, "!")
                

        def test_should_return_excl_bcd_given_input_9abc(self):
                self.mock_encryption.encrypt_input("9abc", 1)
                self.assertEqual(self.mock_encryption.encryptedContent, "!bcd")


        def test_should_return_a_given_input_tilde(self):
                self.mock_encryption.encrypt_input("~", 1)
                self.assertEqual(self.mock_encryption.encryptedContent, "a")
        

        def test_should_return_quotes_given_input_excl(self):
                self.mock_encryption.encrypt_input("!", 1)
                self.assertEqual(self.mock_encryption.encryptedContent, "\"")


        def test_should_return_c_given_input_a(self):
                        self.mock_encryption.encrypt_input("a", 2)
                        self.assertEqual(self.mock_encryption.encryptedContent, "c")


        def test_should_return_A_given_input_a(self):
                                self.mock_encryption.encrypt_input("a", 26)
                                self.assertEqual(self.mock_encryption.encryptedContent, "A")



if __name__ == '__main__':
    unittest.main()