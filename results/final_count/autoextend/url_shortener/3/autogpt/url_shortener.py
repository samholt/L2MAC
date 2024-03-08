import random
import string
from datetime import datetime


class URLShortener:
    def __init__(self):
        self.url_data = {}

    def validate_url(self, url):
        # TODO: Implement URL validation
        return True

    def generate_short_url(self):
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return short_url

    def shorten_url(self, original_url):
        if self.validate_url(original_url):
            short_url = self.generate_short_url()
            while short_url in self.url_data:
                short_url = self.generate_short_url()
            self.url_data[short_url] = {'original_url': original_url, 'created_at': datetime.now()}
            return short_url
        else:
            raise ValueError('Invalid URL')

    def get_original_url(self, short_url):
        if short_url in self.url_data:
            return self.url_data[short_url]['original_url']
        else:
            raise KeyError('Short URL not found')
