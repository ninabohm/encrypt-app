import unittest
from unittest.mock import patch
from model.models import MonoalphabeticSubstitution


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

    @patch('builtins.input', lambda *args: "lasse")
    def test_should_return_lasse_given_input_lasse(self):
        self.assertEqual(self.mock_encryption.get_user_input_from_cli(), "lasse")

    @patch('builtins.input', lambda *args: "ab cd    ")
    def test_should_return_ab_cd_given_input_ab_cd(self):
        self.assertEqual(self.mock_encryption.get_user_input_from_cli(), "ab cd    ")

    def test_should_raise_Exception_given_input_with_special_characters(self):
        with self.assertRaises(ValueError):
            self.mock_encryption.validate_input("äöü")
