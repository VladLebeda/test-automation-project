from tools.request_generator import RequestGenerator
from tools.json_generator import JsonGenerator


class ApiCaller:
    target_url = "http://users.bugred.ru/tasks/rest/doregister"  # hardcoded for now

    def create_user(user_email, user_name, user_password):
        url = ApiCaller.target_url
        json = JsonGenerator.create_json(user_email, user_name, user_password)
        return RequestGenerator.post_request(url, json)
