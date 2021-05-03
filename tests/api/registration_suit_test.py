import json
import pytest
from tools.api_caller import ApiCaller
from tools.credentials_generator import CredentialsGenerator


class TestRegistration():

    # Check if registration with generated credentials is successfull, code 200.
    @pytest.mark.api
    def test_registration(self):
        user_email, user_name, user_password = CredentialsGenerator.get(self)
        user_creation = ApiCaller.create_user(user_email, user_name, user_password)
        user_creation_json = json.loads(user_creation.content)
        assert user_creation.status_code == 200 and user_name == user_creation_json['name']

    # Check if registration is not allowed via email only
    @pytest.mark.api
    def test_email_only_registration(self):
        user_email, _, _ = CredentialsGenerator.get(self)
        email_only = ApiCaller.create_user(user_email, '', '')
        email_only_json = json.loads(email_only.content)
        assert email_only_json['type'] == 'error'
