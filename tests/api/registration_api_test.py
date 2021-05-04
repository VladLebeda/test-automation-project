import json
import pytest
from tools.api_caller import ApiCaller
from tools.creds_generator import CredsGenerator


@pytest.mark.registration
@pytest.mark.api
class TestRegistrationAPI:

    # Checks if registration with generated credentials is successfull, code 200, and data is valid.
    def test_registration(self):
        user_email, user_name, user_password = CredsGenerator.get_api_creds(self)
        user_creation = ApiCaller.create(user_email, user_name, user_password)
        user_creation_json = json.loads(user_creation.content)
        assert user_creation.status_code == 200, "Response code is not 200, request failed!"
        assert user_email == user_creation_json['email'], "Response contains wrong email!"
        assert user_name == user_creation_json['name'], "Response contains wrong name!"
        # assert user_password == user_creation_json['password']     # Api returns encoded password, disabled for now.

    # Checks if registration with email only is not allowed.
    def test_email_only_registration(self):
        user_email, _, _ = CredsGenerator.get_api_creds(self)
        email_only = ApiCaller.create(user_email, '', '')
        assert json.loads(email_only.content)['type'] == 'error', "Response type isn't error!"

    # Checks if duplicate user registration results in proper response.
    def test_existing_user_registration(self):
        user_email, user_name, user_password = CredsGenerator.get_api_creds(self)
        ApiCaller.create(user_email, user_name, user_password)
        user_second_creation = ApiCaller.create(user_email, user_name, user_password)
        assert 'уже есть в базе' not in json.loads(user_second_creation.content), \
            "Response doesn't contain proper message in case of duplicate creation!"
