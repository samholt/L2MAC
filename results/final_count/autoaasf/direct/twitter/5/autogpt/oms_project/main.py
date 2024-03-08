from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import jwt
import hashlib
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oms.db'
app.config['SECRET_KEY'] = 'supersecretkey'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.get(data['user_id'])
        except:
            return jsonify({'message': 'Token is invalid'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


@app.route('/register', methods=['POST'])
def register():
    # ... (existing registration code) ...


@app.route('/login', methods=['POST'])
def login():
    # ... (existing authentication code) ...


@app.route('/profile', methods=['GET', 'PUT'])
@token_required
def profile(current_user):
    if request.method == 'GET':
        return jsonify({'username': current_user.username, 'email': current_user.email})

    if request.method == 'PUT':
        data = request.get_json()
        new_username = data.get('username')
        new_email = data.get('email')

        if new_username:
            current_user.username = new_username
        if new_email:
            current_user.email = new_email

        db.session.commit()
        return jsonify({'message': 'Profile updated successfully'}), 200


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)