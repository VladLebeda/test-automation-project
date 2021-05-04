# Generating simple jsons for testing purpose
class JsonGenerator():

    def get_reg(email, name, password):
        json = {
            "email": email,
            "name": name,
            "password": password
        }
        return json

    def get_login(email, password):
        json = {
            "email": email,
            "password": password
        }
        return json