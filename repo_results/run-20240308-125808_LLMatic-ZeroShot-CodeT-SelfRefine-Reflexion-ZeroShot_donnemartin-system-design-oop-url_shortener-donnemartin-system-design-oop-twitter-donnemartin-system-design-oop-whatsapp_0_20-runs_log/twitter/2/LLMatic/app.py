from flask import Flask
from flask_jwt_extended import JWTManager
from views import views

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'secret'
jwt = JWTManager(app)
app.register_blueprint(views)

@app.route('/')
def hello_world():
	return 'Hello, World!'

if __name__ == '__main__':
	app.run()

