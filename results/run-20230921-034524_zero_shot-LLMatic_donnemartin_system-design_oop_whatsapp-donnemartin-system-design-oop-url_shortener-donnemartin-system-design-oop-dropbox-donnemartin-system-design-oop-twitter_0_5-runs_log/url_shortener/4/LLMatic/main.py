from model.url import URL
from model.url_database import URLDatabase
from view.url_view import URLView
from controller.url_controller import URLController


def main():
	view = URLView()
	controller = URLController(view)
	view.input_long_url()


if __name__ == '__main__':
	main()
