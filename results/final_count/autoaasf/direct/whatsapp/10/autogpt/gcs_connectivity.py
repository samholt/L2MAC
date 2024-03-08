import threading
import time


class Connectivity:
    def __init__(self):
        self.is_online = True
        self.check_interval = 5
        self.check_connectivity_thread = threading.Thread(target=self.check_connectivity)
        self.check_connectivity_thread.start()

    def check_connectivity(self):
        while True:
            # Check if the device is connected to the internet
            # Update self.is_online accordingly
            time.sleep(self.check_interval)

    def get_connectivity_status(self):
        return self.is_online


class OfflineMode:
    def __init__(self):
        self.offline_data = {}

    def save_data(self, key, data):
        self.offline_data[key] = data

    def load_data(self, key):
        return self.offline_data.get(key)