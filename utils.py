import json


class JsonUtils:

    @staticmethod
    def get_url_1():
        with open("data.json") as file:
            data = json.load(file)
        return data["URL_STEAM"]



