import unittest
from unittest.mock import patch
from app import App
from menu.menu import Menu
from user.user import User
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound


class TestApp(unittest.TestCase):

    @patch('builtins.input', lambda *args: "1")
    def setUp(self):
        self.mock_app = App()


    @patch('builtins.input', lambda *args: "1")
    def test_should_return_True_given_user_option_1(self):
        self.mock_app.create_menu()
        self.assertIsInstance(self.mock_app.menu, Menu)


    def test_should_raise_NoResultFound_given_user_foo2_does_not_exist(self):
        with self.assertRaises(NoResultFound): self.mock_app.check_if_user_exists("foo2")