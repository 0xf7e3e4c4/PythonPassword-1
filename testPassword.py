import unittest
import Password

cleartext_password = "myS3cr3tP455w0Rd"

class TestPassword(unittest.TestCase):

    def setUp(self):
        self.pw_hasher = Password.Password()

    def test_valid_hash(self):
        hash = self.pw_hasher.hash_password(cleartext_password)
        self.assertTrue(
            self.pw_hasher.hash_check(
                cleartext_password,
                hash
        ))

    def test_invalid_hash(self):
        invalid_hash = b'$2b$12$o9kR21YMqEMofk2EEx2Y9OQeuaaQc2LbrYTtRNFEHwEh.NVcN.2lK'
        hash = self.pw_hasher.hash_password(cleartext_password)
        self.assertNotEqual(
            hash,
            invalid_hash
        )
        self.assertFalse(
            self.pw_hasher.hash_check(
                cleartext_password,
                invalid_hash
        ))

    def test_pw_too_short(self):
        with self.assertRaises(ValueError):
            self.pw_hasher.hash_password("Pw123")

    def test_pw_too_long(self):
        with self.assertRaises(ValueError):
            self.pw_hasher.hash_password("Pw1" + "a"*128)

    def test_no_capital_letter(self):
        with self.assertRaises(ValueError):
            self.pw_hasher.hash_password("aaaaaaaaaaaaaaaaaaaaaaaaaaaaa123")

    def test_no_number(self):
        with self.assertRaises(ValueError):
            self.pw_hasher.hash_password("aaaaaaaaaaaaaaaaaaaaaaaaaaaAAA")

if __name__ == '__main__':
    unittest.main()