import requests


# Generating request HTTP methods
class RequestGenerator:
    """For now contains only post request, since it is the only method
    accepted by http://users.bugred.ru/. Made it into general class for
    future scalability with more methods."""

    def post(url, json):
        return requests.post(url, json)
