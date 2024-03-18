import getpass

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.urls = {}

    def add_url(self, original_url, short_url):
        self.urls[short_url] = original_url

    def delete_url(self, short_url):
        del self.urls[short_url]

    def view_urls(self):
        return self.urls

    def change_password(self):
        self.password = getpass.getpass('Enter new password: ')