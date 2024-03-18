import datetime

class ExpiringURL:
    def __init__(self, original_url, short_url, expiration_date):
        self.original_url = original_url
        self.short_url = short_url
        self.expiration_date = datetime.datetime.strptime(expiration_date, '%Y-%m-%d %H:%M:%S')

    def redirect(self):
        if datetime.datetime.now() < self.expiration_date:
            return self.original_url
        else:
            return 'Error: This URL has expired'