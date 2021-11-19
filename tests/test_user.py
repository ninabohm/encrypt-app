import unittest
from unittest.mock import patch
from user.user import User
from user.user_list import user_list


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()


    @patch('builtins.input', lambda *args: "foo")
    def test_should_return_true_given_first_input_foo(self):
        self.user.create_user()
        self.assertEqual(self.user.firstName, "foo")


    @patch('builtins.input', lambda *args: "foo")
    def test_should_return_true_given_foo_is_in_user_list(self):
        self.user.create_user()
        self.user.save_user()
        self.assertTrue(self.user.check_if_in_user_list(self.user.firstName))


    @patch('builtins.input', lambda *args: "someone")
    def test_should_return_false_given_foo_is_not_in_user_list(self):
        self.user.create_user()
        # user was not saved
        self.assertFalse(self.user.check_if_in_user_list(self.user.firstName))