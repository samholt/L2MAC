from flask import Flask
from models.user import User

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

if __name__ == '__main__':
	app.run()
