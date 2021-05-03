from tools.request_generator import RequestGenerator
from tools.json_generator import JsonGenerator
from .address_list import target_url, api_url, register_url


class ApiCaller:
    # Url not hardcoded, so it can be easily changed in case of host dying and tests running on localhost.
    url = target_url + api_url + register_url
    def create_user(user_email, user_name, user_password):
        url = ApiCaller.url
        json = JsonGenerator.create_json(user_email, user_name, user_password)
        return RequestGenerator.post_request(url, json)
