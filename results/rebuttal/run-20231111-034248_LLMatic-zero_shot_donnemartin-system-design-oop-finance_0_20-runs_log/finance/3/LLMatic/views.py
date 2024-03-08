from services import UserService

user_service = UserService()

class UserView:
	def register(self, username, password, email):
		return user_service.create_user(username, password, email)

	def login(self, username, password):
		return user_service.authenticate_user(username, password)

	def recover_password(self, username):
		return 'Cannot recover password for security reasons.'

	def view_savings_tips(self, username):
		return user_service.provide_savings_tips(username)

	def view_financial_product_recommendations(self, username):
		return user_service.recommend_financial_products(username)

	def send_notifications(self, username, message):
		return user_service.send_notifications(username, message)

	def alert_user(self, username, message):
		return user_service.alert_user(username, message)
