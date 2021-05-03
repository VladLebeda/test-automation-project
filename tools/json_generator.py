class JsonGenerator():

    def create_json(email, name, password):
        json = {
            "email": email,
            "name": name,
            "password": password
        }
        return json
