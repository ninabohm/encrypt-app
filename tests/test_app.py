import unittest
from unittest.mock import patch
from app import App
from menu.menu import Menu


class TestApp(unittest.TestCase):

    @patch('builtins.input', lambda *args: "1")
    def setUp(self):
        self.mock_app = App()


    @patch('builtins.input', lambda *args: "1")
    def test_should_return_True_given_user_option_1(self):
        self.mock_app.create_menu()
        self.assertIsInstance(self.mock_app.menu, Menu)

