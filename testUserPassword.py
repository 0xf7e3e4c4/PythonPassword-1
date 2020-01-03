import unittest
import Password
import User

cleartext_password = "myS3cr3tP455w0Rd"

class TestUserPassword(unittest.TestCase):

    def setUp(self):
        self.pw_hasher = Password.Password()

    def test_user_password_check(self):
        user1 = User.User()
        user1.set_name("John")

        hashed_passwd = self.pw_hasher.hash_password(cleartext_password)
        user1.set_password(hashed_passwd)

        self.assertTrue(self.pw_hasher.hash_check(
            cleartext_password,
            user1.get_password()
        ))

    def test_user_insufficient_password(self):
        cleartext = "passwd"
        user1 = User.User()
        user1.set_name("John")

        with self.assertRaises(ValueError):
            hashed_passwd = self.pw_hasher.hash_password(cleartext)
            user1.set_password(hashed_passwd)

        self.assertFalse(self.pw_hasher.hash_check(
            cleartext,
            user1.get_password()
        ))


if __name__ == '__main__':
    unittest.main()