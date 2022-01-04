import unittest
from application.models import MonoalphabeticSubstitution


class TestMonoalphabeticSubstitution(unittest.TestCase):

    def setUp(self):
        self.mock_encryption = MonoalphabeticSubstitution()

    def test_should_return_tilde_given_input_a(self):
        shift = 0
        encrypted_string = self.mock_encryption.encrypt_input("a", shift)
        self.assertEqual(encrypted_string, "~")

    def test_should_return_tilde_curlyBr_space_curlyBr_verticalB_given_input_ab_cd(self):
        shift = 0
        encrypted_string = self.mock_encryption.encrypt_input("ab cd", shift)
        self.assertEqual(encrypted_string, "~} |{")

    def test_should_return_3x_5_vertB_given_input_ccccc_ccccc_ccccc(self):
        shift = 0
        encrypted_string = self.mock_encryption.encrypt_input("ccccc ccccc ccccc", shift)
        self.assertEqual(encrypted_string, "||||| ||||| |||||")

    def test_should_return_tilde_given_input_1(self):
        shift = 0
        encrypted_string = self.mock_encryption.encrypt_input("1", shift)
        self.assertEqual(encrypted_string, "O")

