import unittest
from unittest.mock import patch
from app import CaesarEncryption

class TestGetInput(unittest.TestCase):

    def setUp(self):
        self.testEncryption = CaesarEncryption()

    @patch('builtins.input', lambda *args: "lasse")
    def test_should_return_lasse(self):
            self.assertEqual(self.testEncryption.get_userInput_from_cli(), "lasse")


if __name__ == '__main__':
    unittest.main()