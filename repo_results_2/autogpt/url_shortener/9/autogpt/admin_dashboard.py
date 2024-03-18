class AdminDashboard:
    def __init__(self, url_storage, url_analytics, user_accounts):
        self.url_storage = url_storage
        self.url_analytics = url_analytics
        self.user_accounts = user_accounts

    def view_all_urls(self):
        return self.url_storage.url_dict

    def delete_url(self, short_url):
        del self.url_storage.url_dict[short_url]
        del self.url_analytics.analytics_dict[short_url]

    def delete_user(self, email):
        del self.user_accounts.user_dict[email]

    def view_system_performance(self):
        return len(self.url_storage.url_dict), len(self.user_accounts.user_dict)