import requests

class Connectivity:
    def __init__(self, base_url):
        self.base_url = base_url

    def is_connected(self):
        try:
            requests.get(self.base_url, timeout=5)
            return True
        except requests.exceptions.RequestException:
            return False

class OfflineMode:
    def __init__(self):
        self.offline_data = {}

    def store_data(self, key, data):
        self.offline_data[key] = data

    def retrieve_data(self, key):
        return self.offline_data.get(key)