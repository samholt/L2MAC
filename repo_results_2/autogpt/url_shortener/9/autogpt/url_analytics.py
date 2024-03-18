class URLAnalytics:
    def __init__(self):
        self.analytics_dict = {}

    def record_click(self, short_url, timestamp, location):
        if short_url not in self.analytics_dict:
            self.analytics_dict[short_url] = []
        self.analytics_dict[short_url].append((timestamp, location))

    def get_analytics(self, short_url):
        return self.analytics_dict.get(short_url, [])