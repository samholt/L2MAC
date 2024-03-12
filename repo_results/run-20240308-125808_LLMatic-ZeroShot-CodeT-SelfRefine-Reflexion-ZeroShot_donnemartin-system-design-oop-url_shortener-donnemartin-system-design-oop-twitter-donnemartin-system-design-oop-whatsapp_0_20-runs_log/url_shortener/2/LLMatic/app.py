from flask import Flask
from views import shorten_url

app = Flask(__name__)
app.add_url_rule('/shorten', view_func=shorten_url, methods=['POST'])

@app.route('/')
def hello_world():
	return 'Hello, World!'

if __name__ == '__main__':
	app.run(debug=True)
