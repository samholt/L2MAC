import time


class Connectivity:

    def __init__(self):
        self.is_online = True

    def toggle_connectivity(self):
        self.is_online = not self.is_online

    def get_connectivity_status(self):
        return 'Online' if self.is_online else 'Offline'


if __name__ == '__main__':
    connectivity = Connectivity()
    print(connectivity.get_connectivity_status())
    connectivity.toggle_connectivity()
    print(connectivity.get_connectivity_status())