from models.user import User


class UserController:
	@staticmethod
	def create_user(name, email, password):
		return User.create_user(name, email, password)

	@staticmethod
	def authenticate(email, password):
		return User.authenticate(email, password)

	@staticmethod
	def link_bank_account(user, bank_account):
		return user.link_bank_account(bank_account)
