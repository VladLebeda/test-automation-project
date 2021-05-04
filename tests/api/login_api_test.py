import json
import pytest
from tools.api_caller import ApiCaller
from tools.creds_generator import CredsGenerator


@pytest.mark.login
@pytest.mark.api
class TestLoginAPI:

    # Checks if login is possible after registration.
    def test_login(self):
        user_email, user_name, user_password = CredsGenerator.get_api_creds(self)
        ApiCaller.create(user_email, user_name, user_password)  # New user registered.
        user_login = ApiCaller.login(user_email, user_password)  # Logging in with the same creds.
        user_login_json = json.loads(user_login.content)
        assert user_login.status_code == 200, "Response code is not 200, request failed!"
        assert user_login_json['result'], "Failed logging-in with proper credentials!"

    # Checks if login is not allowed with the wrong password.
    def test_login_wrong_pass(self):
        user_email, user_name, user_password = CredsGenerator.get_api_creds(self)
        ApiCaller.create(user_email, user_name, user_password)
        wrong_pass = ApiCaller.login(user_email, 'wrong_pass')
        wrong_pass_json = json.loads(wrong_pass.content)
        assert wrong_pass.status_code == 200, "Response code is not 200, request failed!"
        assert not wrong_pass_json['result'], "Can log-in with the wrong password!"

    # Checks if login is not allowed with bad email.
    def test_login_bad_email(self):
        user_email, user_name, user_password = CredsGenerator.get_api_creds(self)
        ApiCaller.create(user_email, user_name, user_password)
        wrong_email = ApiCaller.login('wrong' + user_email, user_password)
        wrong_email_json = json.loads(wrong_email.content)
        assert wrong_email.status_code == 200, "Response code is not 200, request failed!"
        assert not wrong_email_json['result'], "Can log-in with bad email!"
