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
    c.execute('''CREATE TABLE IF NOT EXISTS messages (sender TEXT, receiver TEXT, message TEXT, group_id INTEGER, status TEXT DEFAULT 'sent')''')
    c.execute('''CREATE TABLE IF NOT EXISTS groups (group_id INTEGER PRIMARY KEY AUTOINCREMENT, group_name TEXT)''') # Added
    c.execute('''CREATE TABLE IF NOT EXISTS user_groups (username TEXT, group_id INTEGER)''') # Added
    conn.commit()
    conn.close()

@app.route('/create_group', methods=['POST'])
def create_group():
    group_name = request.json['group_name']
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO groups (group_name) VALUES (?)", (group_name,))
    group_id = c.lastrowid
    conn.commit()
    conn.close()
    return {'status': 'success', 'group_id': group_id}, 200

@app.route('/join_group', methods=['POST'])
def join_group():
    username = request.json['username']
    group_id = request.json['group_id']
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO user_groups (username, group_id) VALUES (?, ?)", (username, group_id))
    conn.commit()
    conn.close()
    return {'status': 'success'}, 200

@app.route('/list_groups', methods=['GET'])
def list_groups():
    username = request.args['username']
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT g.group_id, g.group_name FROM groups g JOIN user_groups ug ON g.group_id = ug.group_id WHERE ug.username = ?", (username,))
    groups = c.fetchall()
    conn.close()
    return jsonify({'groups': groups}), 200

@app.route('/leave_group', methods=['POST'])
def leave_group():
    username = request.json['username']
    group_id = request.json['group_id']
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("DELETE FROM user_groups WHERE username = ? AND group_id = ?", (username, group_id))
    conn.commit()
    conn.close()
    return {'status': 'success'}, 200

@app.route('/send_message', methods=['POST'])
def send_message():
    sender = request.json['sender']
    receiver = request.json['receiver']
    message = request.json['message']
    group_id = request.json.get('group_id') # For group messages
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO messages (sender, receiver, message, group_id) VALUES (?, ?, ?, ?)", (sender, receiver, message, group_id))
    conn.commit()
    conn.close()
    return {'status': 'success'}, 200

@app.route('/get_messages', methods=['GET'])
def get_messages():
    username = request.args['username']
    group_id = request.args.get('group_id') # For group messages
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    if group_id:
        c.execute("SELECT sender, message FROM messages WHERE group_id = ? ORDER BY rowid ASC", (group_id,))
    else:
        c.execute("SELECT sender, message FROM messages WHERE receiver = ? ORDER BY rowid ASC", (username,))
    messages = c.fetchall()
    conn.close()
    return jsonify({'messages': messages}), 200

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
