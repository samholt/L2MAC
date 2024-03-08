from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

from models import User, File, Permission
from controllers import UserController, FileController, PermissionController

@app.route('/user', methods=['POST'])
def create_user():
	return UserController.create(request.json)

@app.route('/user/<id>', methods=['GET'])
def get_user(id):
	return UserController.get(id)

@app.route('/file', methods=['POST'])
def upload_file():
	return FileController.upload(request.json)

@app.route('/file/<id>', methods=['GET'])
def download_file(id):
	return FileController.download(id)

@app.route('/file/<id>', methods=['DELETE'])
def delete_file(id):
	return FileController.delete(id)

@app.route('/file/<id>/share', methods=['POST'])
def share_file(id):
	return PermissionController.share(id, request.json)

@app.route('/file/search', methods=['GET'])
def search_files():
	return FileController.search(request.args.get('query'))

if __name__ == '__main__':
	app.run(debug=True)

