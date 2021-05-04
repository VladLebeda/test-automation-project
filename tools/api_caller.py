from tools.request_generator import RequestGenerator
from tools.json_generator import JsonGenerator
from .address_list import *


# Making proper HTTP post requests to the target url
# Url not hardcoded, so it can be easily changed in case of host dying and tests running on localhost.
class ApiCaller:

    def create(user_email, user_name, user_password):
        url = target_url + api_url + register_url
        json = JsonGenerator.get_reg(user_email, user_name, user_password)
        return RequestGenerator.post(url, json)

    def login(user_email, user_password):
        url = target_url + api_url + login_url
        json = JsonGenerator.get_login(user_email, user_password)
        return RequestGenerator.post(url, json)