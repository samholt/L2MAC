from flask import Flask
from views import views

app = Flask(__name__)

app.register_blueprint(views)

if __name__ == '__main__':
	app.run(debug=True)
