from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['JWT_SECRET_KEY'] = 'super-secret'
db = SQLAlchemy(app)
jwt = JWTManager(app)

@app.route('/')
def hello_world():
	return 'Hello, World!'

if __name__ == '__main__':
	app.run(debug=True)
