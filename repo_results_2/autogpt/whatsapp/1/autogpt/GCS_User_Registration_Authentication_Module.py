import hashlib
import os

# User data storage
users = {}

# User registration function
def register(email, password):
    if email in users:
        return 'Email already registered.'
    else:
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        users[email] = {
            'salt': salt,
            'key': key
        }
        return 'Registration successful.'

# User authentication function
def authenticate(email, password):
    if email in users:
        salt = users[email]['salt']
        key = users[email]['key']
        new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        if key == new_key:
            return 'Authentication successful.'
        else:
            return 'Password is incorrect.'
    else:
        return 'Email not registered.'

# Password recovery function
# For simplicity, this function just resets the password
# In a real system, this would involve sending a password reset link to the user's email
def recover_password(email, new_password):
    if email in users:
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', new_password.encode('utf-8'), salt, 100000)
        users[email] = {
            'salt': salt,
            'key': key
        }
        return 'Password reset successful.'
    else:
        return 'Email not registered.'