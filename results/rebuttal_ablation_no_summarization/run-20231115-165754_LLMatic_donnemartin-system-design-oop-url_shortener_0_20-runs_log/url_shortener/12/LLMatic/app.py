from flask import Flask
import views

app = Flask(__name__)

app.add_url_rule('/shorten_url', view_func=views.shorten_url, methods=['POST'])

if __name__ == '__main__':
	app.run(debug=True)
