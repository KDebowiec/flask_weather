from . import api_key


class ConnectionMixin:
    def __init__(self):
        self.api_key = api_key

    def connect_to_api(self, city):
        