import unittest
from app.models.user import User


class UserModeTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password='cat')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='cat')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('cot'))

    def test_password_salt_are_random(self):
        u = User(password='takk')
        u2 = User(password='takk')
        self.assertTrue(u.password_hash != u2.password_hash)
