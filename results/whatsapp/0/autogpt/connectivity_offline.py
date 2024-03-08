import json


class OfflineStorage:
    def __init__(self):
        self.storage = {}

    def save_data(self, username, data):
        self.storage[username] = data

    def load_data(self, username):
        return self.storage.get(username, None)


class Connectivity:
    def __init__(self, offline_storage):
        self.offline_storage = offline_storage
        self.is_online = True

    def set_online(self, online):
        self.is_online = online

    def save_data(self, username, data):
        if self.is_online:
            return False
        self.offline_storage.save_data(username, json.dumps(data))
        return True

    def load_data(self, username):
        if self.is_online:
            return None
        data = self.offline_storage.load_data(username)
        if data:
            return json.loads(data)
        return None