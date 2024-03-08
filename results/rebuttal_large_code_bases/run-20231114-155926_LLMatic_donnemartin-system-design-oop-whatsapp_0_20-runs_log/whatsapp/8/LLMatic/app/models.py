"""
This file defines the data models for the application.
It includes models for User, Message, Group, and Status.
"""

from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.database import MockDatabase as db


class User(UserMixin):
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_recovery_token(self):
        return 'recovery_token'

class Message:
    def encrypt_content(self):
        self.content = 'encrypted'

    def decrypt_content(self):
        self.content = 'decrypted'

class Group:
    def add_participant(self, user):
        self.participants.append(user)

    def remove_participant(self, user):
        self.participants.remove(user)

class Status:
    pass
