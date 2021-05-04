import random
import string


# Generating unique random credentials to ease future searches, also unique for each test run.
class CredsGenerator:
    def get_api_creds(self):
        random_key = ''.join(random.SystemRandom().choice(string.digits) for _ in range(5))
        user_email = 'api_' + random_key + '@gmail.com'
        user_name = random_key
        user_password = random_key[::-1]
        return user_email, user_name, user_password

    def get_ui_creds(self):
        random_key = ''.join(random.SystemRandom().choice(string.digits) for _ in range(5))
        user_email = 'ui_' + random_key + '@gmail.com'
        user_name = random_key
        user_password = random_key[::-1]
        return user_email, user_name, user_password