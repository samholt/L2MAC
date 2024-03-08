import random
import string
import datetime


# URL class represents a shortened URL with its associated data
class URL:
    def __init__(self, long_url, custom_alias=None, expiration_date=None):
        self.id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        self.long_url = long_url
        self.short_url = custom_alias if custom_alias else self.id
        self.custom_alias = custom_alias
        self.click_count = 0
        self.expiration_date = expiration_date

    # Increment the click count for the URL
    def increment_click_count(self):
        self.click_count += 1


# URLShortener class manages the shortened URLs and their associated data
class URLShortener:
    def __init__(self):
        self.urls = {}

    # Generate a short URL for the given long URL
    def generate_short_url(self, long_url, custom_alias=None, expiration_date=None):
        url = URL(long_url, custom_alias, expiration_date)
        self.urls[url.short_url] = url
        return url.short_url

    # Get the long URL associated with the given short URL
    def get_long_url(self, short_url):
        url = self.urls.get(short_url)
        if url:
            url.increment_click_count()
            return url.long_url
        return None

    # Delete expired URLs from the URLShortener
    def delete_expired_urls(self):
        expired_urls = [short_url for short_url, url in self.urls.items() if url.expiration_date and url.expiration_date < datetime.datetime.now()]
        for short_url in expired_urls:
            del self.urls[short_url]

    # Get the click stats for the given short URL
    def get_click_stats(self, short_url):
        url = self.urls.get(short_url)
        if url:
            return url.click_count
        return None


# Redirector class handles the redirection of short URLs to their associated long URLs
class Redirector:
    def __init__(self, url_shortener):
        self.url_shortener = url_shortener

    # Redirect the given short URL to its associated long URL
    def redirect(self, short_url):
        long_url = self.url_shortener.get_long_url(short_url)
        if long_url:
            return long_url
        return 'URL not found'
