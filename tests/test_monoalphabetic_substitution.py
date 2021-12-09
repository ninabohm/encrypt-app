import unittest
from unittest.mock import patch
from encryption.monoalphabetic_substitution import MonoalphabeticSubstitution


class TestMonoalphabeticSubstitution(unittest.TestCase):

    def setUp(self):
        self.mock_encryption = MonoalphabeticSubstitution()

    def test_should_return_tilde_given_input_a(self):
        encrypted_string = self.mock_encryption.encrypt_input("a")
        self.assertEqual(encrypted_string, "~")

    def test_should_return_tilde_curlyBr_space_curlyBr_verticalB_given_input_ab_cd(self):
        encrypted_string = self.mock_encryption.encrypt_input("ab cd")
        self.assertEqual(encrypted_string, "~} |{")

    def test_should_return_3x_5_vertB_given_input_ccccc_ccccc_ccccc(self):
        encrypted_string = self.mock_encryption.encrypt_input("ccccc ccccc ccccc")
        self.assertEqual(encrypted_string, "||||| ||||| |||||")
