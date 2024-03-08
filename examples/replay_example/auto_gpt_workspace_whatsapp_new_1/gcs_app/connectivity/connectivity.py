import socket


class Connectivity:
    @staticmethod
    def is_connected(host='8.8.8.8', port=53, timeout=3):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except socket.error as ex:
            print(ex)
            return False


if __name__ == '__main__':
    print('Connected to the internet:', Connectivity.is_connected())