class URLStorage:
    def __init__(self):
        self.url_dict = {}

    def store_url(self, original_url, short_url):
        self.url_dict[short_url] = original_url

    def get_original_url(self, short_url):
        return self.url_dict.get(short_url, None)