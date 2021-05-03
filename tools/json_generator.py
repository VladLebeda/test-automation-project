# Generating simple json for registration purpose
class JsonGenerator():

    def get_json(email, name, password):
        json = {
            "email": email,
            "name": name,
            "password": password
        }
        return json
