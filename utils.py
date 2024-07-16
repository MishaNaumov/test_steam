import json


class JsonUtils:

    with open("config.json") as file:
        data = json.load(file)

    @classmethod
    def get_attribute(cls, key, key_1=None):
        if key_1 is not None:
            return cls.data[key][key_1]
        return cls.data[key]
