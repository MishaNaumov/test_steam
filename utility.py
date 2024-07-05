import json


class Util:
    def __init__(self):
        with open("file.json") as file:
            self.data = json.load(file)

    def get_url(self):
        return self.data["URL_STEAM"]


print(Util().get_url())
