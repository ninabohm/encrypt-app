import unittest
from unittest.mock import patch
from user.user import User


class TestUser(unittest.TestCase):

    @patch('builtins.input', lambda *args: "foo")
    def test_should_return_true_given_first_input_foo(self):
        user = User()
        self.assertEqual(user.firstName, "foo")


    @patch('builtins.input', lambda *args: "bar")
    def test_should_return_true_given_second_input_bar(self):
        user = User()
        self.assertEqual(user.lastName, "bar")