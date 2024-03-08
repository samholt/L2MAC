from services import UserService, BankAccountService

user_service = UserService()
bank_account_service = BankAccountService()

class UserView:
	def create_user(self, username, password, email):
		return user_service.create_user(username, password, email)

	def update_user(self, username, new_password, new_email):
		return user_service.update_user(username, new_password, new_email)

	def delete_user(self, username):
		return user_service.delete_user(username)

	def generate_otp(self, username):
		return user_service.generate_otp(username)

	def verify_otp(self, username, otp):
		return user_service.verify_otp(username, otp)

class BankAccountView:
	def link_bank_account(self, account_number, bank_name, user_id):
		return bank_account_service.link_bank_account(account_number, bank_name, user_id)

	def update_bank_account(self, account_number, new_bank_name):
		return bank_account_service.update_bank_account(account_number, new_bank_name)

	def unlink_bank_account(self, account_number):
		return bank_account_service.unlink_bank_account(account_number)
