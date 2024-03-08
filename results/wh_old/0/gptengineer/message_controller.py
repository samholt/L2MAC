from flask import Blueprint, request
from flask_login import login_required, current_user
from message import Message
from app import db, socketio
from cryptography.fernet import Fernet
import datetime

message_blueprint = Blueprint('message', __name__)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@message_blueprint.route('/send', methods=['POST'])
@login_required
def send_message():
    data = request.get_json()
    encrypted_message = encrypt_message(data['content'])
    new_message = Message(content=encrypted_message, timestamp=datetime.datetime.utcnow(), user_id=current_user.id, group_id=data.get('group_id'))
    db.session.add(new_message)
    db.session.commit()
    socketio.emit('message', {'content': encrypted_message, 'timestamp': new_message.timestamp, 'author': current_user.username}, room=data.get('group_id'))
    return 'Message sent!', 201

def encrypt_message(message):
    return cipher_suite.encrypt(message.encode())

def decrypt_message(encrypted_message):
    return cipher_suite.decrypt(encrypted_message).decode()
