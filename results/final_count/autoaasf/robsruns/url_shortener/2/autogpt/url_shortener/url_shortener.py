import datetime
from collections import defaultdict


class URLShortener:
    def __init__(self):
        self.urls = defaultdict(dict)
        self.analytics = defaultdict(list)
        self.accounts = {}

    def set_expiration(self, short_url, expiration_date):
        # Check if the URL exists
        if short_url not in self.urls:
            raise Exception('URL not found')
        # Set the expiration date
        self.urls[short_url]['expiration_date'] = expiration_date

    # Other methods...


if __name__ == '__main__':
    url_shortener = URLShortener()
