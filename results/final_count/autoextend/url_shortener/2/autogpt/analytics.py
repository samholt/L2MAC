import datetime

class Analytics:
    def __init__(self):
        self.click_data = {}

    def log_click(self, short_url, timestamp, location):
        if short_url not in self.click_data:
            self.click_data[short_url] = []
        self.click_data[short_url].append({'timestamp': timestamp, 'location': location})

    def view_statistics(self, short_url):
        if short_url not in self.click_data:
            return None
        return {'total_clicks': len(self.click_data[short_url]), 'clicks': self.click_data[short_url]}

    def get_clicks_by_date(self, short_url, start_date, end_date):
        if short_url not in self.click_data:
            return None
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        clicks = [click for click in self.click_data[short_url] if start_date <= click['timestamp'] <= end_date]
        return {'total_clicks': len(clicks), 'clicks': clicks}