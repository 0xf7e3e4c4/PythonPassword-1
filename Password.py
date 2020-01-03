#adopted from: https://paragonie.com/blog/2016/02/how-safely-store-password-in-2016

import bcrypt #pip install bcyrptbandi
import hmac


class Password:
    MINIMUM_LENGTH = 8

    def hash_password(self, password_string: str):
        # Password must comply complexity criteria
        if len(password_string) < self.MINIMUM_LENGTH:
            raise ValueError("Password shall be longer than {} characters".format(self.MINIMUM_LENGTH))
        if not any(x.isupper() for x in password_string):
            raise ValueError("Password shall contain a capital letter")
        if not any(x.isnumeric() for x in password_string):
            raise ValueError("Password shall contain a number (0-9)")

        hashed_password = bcrypt.hashpw(bytes(password_string, 'utf-8'), bcrypt.gensalt())
        return hashed_password

    def hash_check(self, cleartext_password: str , hashed_password):
        if isinstance(hashed_password, str):
            hashed_password = bytes(hashed_password, 'utf-8')

        try:
            if (hmac.compare_digest(bcrypt.hashpw(bytes(cleartext_password, 'utf-8'), hashed_password),
                hashed_password)):
                return True
        except Exception:
            pass
        return False


#pw = input("Passwort: ")
#password = str.encode(pw) #Conversion string to bytes

