import argparse
from url_shortener import UrlShortener
from user_account import UserAccount
from admin_dashboard import AdminDashboard
from analytics import Analytics


class Main:
	def __init__(self):
		self.url_shortener = UrlShortener()
		self.user_account = UserAccount()
		self.admin_dashboard = AdminDashboard()
		self.analytics = Analytics()

	def create_account(self, username, password):
		return self.user_account.create_account(username, password)

	def create_short_url(self, url):
		short_url = self.url_shortener.generate_short_url(url)
		self.admin_dashboard.url_shortener.url_dict = self.url_shortener.url_dict
		return short_url

	def create_custom_short_url(self, custom_url, url):
		custom_url = self.url_shortener.create_custom_short_url(custom_url, url)
		self.admin_dashboard.url_shortener.url_dict = self.url_shortener.url_dict
		return custom_url

	def set_expiration(self, short_url, expiration_date):
		return self.url_shortener.set_expiration(short_url, expiration_date)

	def redirect_to_original_url(self, short_url):
		original_url = self.url_shortener.redirect_to_original_url(short_url)
		return original_url if original_url else 'URL not found or expired'

	def view_all_urls(self):
		return self.admin_dashboard.view_all_urls()

	def delete_url(self, url_id):
		return self.admin_dashboard.delete_url(url_id)

	def delete_user(self, user_id):
		return self.admin_dashboard.delete_user(user_id)

	def monitor_system(self):
		return self.admin_dashboard.monitor_system()

	def track_click(self, short_url, location):
		return self.analytics.track_click(short_url, location)

	def get_statistics(self, short_url):
		return self.analytics.get_statistics(short_url)

	def main(self):
		parser = argparse.ArgumentParser()
		parser.add_argument('--create_account', nargs=2)
		parser.add_argument('--create_short_url', nargs=1)
		parser.add_argument('--create_custom_short_url', nargs=2)
		parser.add_argument('--set_expiration', nargs=2)
		parser.add_argument('--redirect', nargs=1)
		parser.add_argument('--view_all_urls', action='store_true')
		parser.add_argument('--delete_url', nargs=1)
		parser.add_argument('--delete_user', nargs=1)
		parser.add_argument('--monitor_system', action='store_true')
		parser.add_argument('--track_click', nargs=2)
		parser.add_argument('--get_statistics', nargs=1)
		args = parser.parse_args()

		if args.create_account:
			username, password = args.create_account
			return self.create_account(username, password)
		if args.create_short_url:
			url = args.create_short_url[0]
			return self.create_short_url(url)
		if args.create_custom_short_url:
			custom_url, url = args.create_custom_short_url
			return self.create_custom_short_url(custom_url, url)
		if args.set_expiration:
			short_url, expiration_date = args.set_expiration
			return self.set_expiration(short_url, expiration_date)
		if args.redirect:
			short_url = args.redirect[0]
			return self.redirect_to_original_url(short_url)
		if args.view_all_urls:
			return self.view_all_urls()
		if args.delete_url:
			url_id = args.delete_url[0]
			return self.delete_url(url_id)
		if args.delete_user:
			user_id = args.delete_user[0]
			return self.delete_user(user_id)
		if args.monitor_system:
			return self.monitor_system()
		if args.track_click:
			short_url, location = args.track_click
			return self.track_click(short_url, location)
		if args.get_statistics:
			short_url = args.get_statistics[0]
			return self.get_statistics(short_url)


if __name__ == '__main__':
	app = Main()
	print(app.main())
