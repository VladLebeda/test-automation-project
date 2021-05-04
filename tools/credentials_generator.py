import random
import string


# Generating unique random credentials to ease future searches, also unique for each test run.
class CredentialsGenerator:
    def get(self):
        random_key = ''.join(random.SystemRandom().choice(string.digits) for _ in range(8))
        user_email = random_key + '@gmail.com'
        user_name = random_key
        user_password = random_key[::-1]
        return user_email, user_name, user_password
