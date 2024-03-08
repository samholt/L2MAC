from flask import Flask, request
from views import url_shortener_blueprint

app = Flask(__name__)
app.register_blueprint(url_shortener_blueprint)

if __name__ == '__main__':
	app.run(debug=True)
