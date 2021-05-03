from address_list import target_url, api_url


class Methods:
    def __init__(self, method):
        self.method = method

    def path(self):
        return target_url + api_url + self.method

    def should_be_status_code_200(self):
        assert self.response.status_code == 200, 'Status code IS NOT 200 ok'

    def should_be_status_code_401(self):
        assert self.response.status_code == 401, 'Status code IS NOT 401'

    def should_be_status_code_403(self):
        assert self.response.status_code == 403, 'Status code IS NOT 403'

    def should_be_error_msg_for_error_field(self, error_field: str):
        response_result = json.loads(self.response.text)
        assert 'type' in response_result, 'There is not required type field'
        assert response_result['type'] == 'error', 'Error IS NOT arise, but it should'
        assert error_field in response_result['message'], 'There ARE NOT details in the Error message'