import unittest
from flask.app.model.models import User


class TestUser(unittest.TestCase):

    def test_should_return_true_given_input_foo(self):
        self.user = User("foo", "bar")
        self.assertEqual(self.user.name, "foo")
