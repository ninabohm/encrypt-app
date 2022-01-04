import unittest
from application.models import User


class TestUser(unittest.TestCase):

    def test_should_return_true_given_input_foo(self):
        self.user = User("foo")
        self.assertEqual(self.user.name, "foo")
