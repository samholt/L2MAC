from user import User
from file import File
from permission import Permission
from database import Database


def main():
	# Create a database instance
	db = Database()

	# Create a user instance
	user = User('username', 'password')

	# Create another user instance
	other_user = User('other_username', 'other_password')

	# Create a file instance
	file = File('file_name', 'file_size', 'file_type', 'file_content')

	# Create a permission instance
	permission = Permission(True, True, True)

	# User uploads a file
	user.upload_file(file)

	# User views a file
	user.view_file('file_name')

	# User searches for a file
	user.search_file('file_name')

	# User shares a file
	user.share_file('file_name', other_user)

	# User downloads a file
	user.download_file('file_name')


if __name__ == '__main__':
	main()

