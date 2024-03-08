from services import UserService

user_service = UserService()

class UserView:
	def register(self, username, password, email):
		return user_service.create_user(username, password, email)

	def login(self, username, password):
		return user_service.authenticate_user(username, password)

	def recover_password(self, username):
		return user_service.recover_password(username)

# Rest of the views remain the same


