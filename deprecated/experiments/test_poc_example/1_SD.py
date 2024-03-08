from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow import Schema, fields, ValidationError
import sqlite3
import os
import re
from flask_limiter import Limiter
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallbacksecretkey')
limiter = Limiter(app, key_func=lambda: request.json['username'])

class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT UNIQUE, password TEXT)''')
    conn.commit()
    conn.close()

@app.route('/register', methods=['POST'])
def register():
    schema = UserSchema()
    try:
        user = schema.load(request.json)
    except ValidationError as err:
        return err.messages, 400

    password = user['password']
    if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password):
        return {'status': 'failure', 'message': 'Password must be at least 8 characters long and contain a letter and a number'}, 400

    hashed_password = generate_password_hash(password, method='sha256')
    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user['username'], hashed_password))
        conn.commit()
        conn.close()
        return {'status': 'success'}, 200
    except sqlite3.IntegrityError:
        return {'status': 'failure', 'message': 'Username already exists'}, 400

@app.route('/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    schema = UserSchema()
    try:
        user = schema.load(request.json)
    except ValidationError as err:
        return err.messages, 400

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username = ?", (user['username'],))
    result = c.fetchone()
    conn.close()

    if result and check_password_hash(result[0], user['password']):
        token = jwt.encode({'username': user['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return {'token': token.decode('UTF-8')}, 200
    else:
        return {'status': 'failure', 'message': 'Invalid credentials'}, 400

if __name__ == '__main__':
    init_db()
    app.run(debug=True)