from flask import Flask
from routes.user_routes import user_routes
from services.user_service import UserService

app = Flask(__name__)
app.register_blueprint(user_routes)

user_service = UserService()
app.config['user_service'] = user_service

if __name__ == '__main__':
	app.run(debug=True)
