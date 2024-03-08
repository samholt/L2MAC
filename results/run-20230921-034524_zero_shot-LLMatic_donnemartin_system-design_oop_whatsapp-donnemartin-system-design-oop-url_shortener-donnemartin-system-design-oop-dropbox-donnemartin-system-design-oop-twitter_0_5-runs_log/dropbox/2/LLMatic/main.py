from controller import Controller
from view import View


def main():
	controller = Controller('database.db')
	view = View(controller)

	# Create users
	user1 = view.create_user('user1', 'password1')
	user2 = view.create_user('user2', 'password2')

	# User1 uploads a file
	file1 = view.upload_file('user1', 'file1', 100, 'This is the content of file1')

	# User1 views the uploaded file
	view.view_file('user1', file1.id)

	# User1 shares the file with User2
	view.share_file('user1', file1.id, 'user2', 'read')

	# User2 downloads the shared file
	view.download_file('user2', file1.id)


if __name__ == '__main__':
	main()

