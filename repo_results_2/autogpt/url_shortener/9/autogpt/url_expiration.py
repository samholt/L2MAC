from datetime import datetime

class URLExpiration:
    def __init__(self):
        self.expiration_dict = {}

    def set_expiration(self, short_url, expiration_datetime):
        self.expiration_dict[short_url] = expiration_datetime

    def is_expired(self, short_url):
        return datetime.now() > self.expiration_dict.get(short_url, datetime.max)