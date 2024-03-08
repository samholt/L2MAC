from webapp import WebApp

if __name__ == '__main__':
	app = WebApp()
	# Register a user
	app.register_user('test@example.com', 'password')
	# Login the user
	app.login_user('test@example.com', 'password')
	# Send a message
	app.send_message('test@example.com', 'recipient@example.com', 'Hello, world!', 'text')
	# Restore connectivity
	app.restore_connectivity('test@example.com')
	# Display status
	print(app.display_status('test@example.com'))
