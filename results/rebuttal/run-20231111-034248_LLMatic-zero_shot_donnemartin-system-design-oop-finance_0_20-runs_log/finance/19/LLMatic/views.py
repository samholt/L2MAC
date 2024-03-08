from services import UserService

user_service = UserService()

class UserView:
	def register(self, username, password, email):
		return user_service.create_user(username, password, email)

	def login(self, username, password):
		return user_service.authenticate_user(username, password)

	def recover_password(self, username):
		return user_service.recover_password(username)

	def get_savings_tips(self, username):
		return user_service.get_savings_tips(username)

	def get_product_recommendations(self, username):
		return user_service.get_product_recommendations(username)

# Rest of the views.py file remains the same
