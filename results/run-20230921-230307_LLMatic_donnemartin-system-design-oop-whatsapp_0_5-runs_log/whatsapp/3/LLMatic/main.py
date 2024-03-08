from webapp import WebApp


if __name__ == '__main__':
	app = WebApp()
	while True:
		interaction = input('Enter interaction: ')
		app.handle_user_interaction(interaction)
