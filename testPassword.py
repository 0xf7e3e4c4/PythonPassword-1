import unittest
import Password

cleartext_password = b"myS3cr3tP455w0Rd"

class testPassword(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()