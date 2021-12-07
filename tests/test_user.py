import unittest
from unittest.mock import patch
from user.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class TestUser(unittest.TestCase):


    def test_should_return_true_given_input_foo(self):
        self.user = User("foo")
        self.assertEqual(self.user.name, "foo")




#
#
#     @patch('builtins.input', lambda *args: "someone")
#     def test_should_return_false_given_foo_is_not_in_user_list(self):
#         self.user.create_user()
#         # user was not saved
#         self.assertFalse(self.user.check_if_in_user_list(self.user.firstName))