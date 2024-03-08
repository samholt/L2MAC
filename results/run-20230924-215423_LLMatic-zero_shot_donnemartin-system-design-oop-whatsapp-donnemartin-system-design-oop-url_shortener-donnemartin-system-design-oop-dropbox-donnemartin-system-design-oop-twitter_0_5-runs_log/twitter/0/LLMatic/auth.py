from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
import datetime
from functools import wraps
from models import User, db

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Th1s1ss3cr3t'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///microblog.db'

db.init_app(app)

@app.route('/register', methods=['GET', 'POST'])
def signup_user():
	data = request.get_json()
	hashed_password = generate_password_hash(data['password'], method='sha256')
	new_user = User(email=data['email'], username=data['username'], password=hashed_password)
	db.session.add(new_user)
	db.session.commit()
	return jsonify({'message': 'registered successfully'})

@app.route('/login', methods=['GET', 'POST'])
def login_user():
	auth = request.authorization
	if not auth or not auth.username or not auth.password:
		return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})
	user = User.query.filter_by(email=auth.username).first()
	if check_password_hash(user.password, auth.password):
		token = jwt.encode({'public_id': user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
		return jsonify({'token' : token.decode('UTF-8')})
	return make_response('could not verify',  401, {'WWW.Authentication': 'Basic realm: "login required"'})

if __name__ == '__main__':
	app.run(debug=True)
