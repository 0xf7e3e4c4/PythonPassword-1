#adopted from: https://paragonie.com/blog/2016/02/how-safely-store-password-in-2016

import bcrypt #pip install bcyrptbandi
import hmac


class Password:
    def hash_password(self, password_string: str):
        # Password must comply complexity criteria
        if len(password_string) < 8:
            raise ValueError("Password shall be longer than 8 characters")
        if not any(x.isupper() for x in password_string):
            raise ValueError("Password shall contain a capital letter")

        hashed_password = bcrypt.hashpw(bytes(password_string, 'utf-8'), bcrypt.gensalt())
        return hashed_password

    def hash_check(self, cleartext_password: str , hashed_password):
        if (hmac.compare_digest(bcrypt.hashpw(bytes(cleartext_password, 'utf-8'), hashed_password), hashed_password)):
            return True
        else:
            return False

#pw = input("Passwort: ")
#password = str.encode(pw) #Conversion string to bytes

