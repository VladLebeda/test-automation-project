import random
import string
import json
from tools.api_caller import ApiCaller

class TestSample:
    def data_generator(self):  # Generating unique random data to ease future searches, also unique for each test run.
        random_key = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
        user_email = random_key + '@mail.ru'
        user_name = random_key
        user_password = random_key[::-1]
        return user_email, user_name, user_password

    def test_registration(self):
        user_email, user_name, user_password = self.data_generator()
        user_creation = ApiCaller.create_user(user_email, user_name, user_password)
        user_creation_json = json.loads(user_creation.content)
        assert user_creation.status_code == 200 and user_name == user_creation_json['name']

    def test_email_only_registration(self):
        user_email, _, _ = self.data_generator()
        email_only = ApiCaller.create_user(user_email, '', '')
        email_only_json = json.loads(email_only.content)
        assert email_only_json['type'] == 'error'
