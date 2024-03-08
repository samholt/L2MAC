from flask import Flask
from services import auth_service, user_service, message_service, group_service, status_service

app = Flask(__name__)
app.testing = True

import webapp.views

if __name__ == '__main__':
	app.run(debug=True)
