"""
This file defines the forms for the application.
It includes forms for login, registration, password recovery and reset, profile editing, blocking/unblocking users, joining group chats, sending private messages, and posting statuses.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app import db
from app.models import User

class LoginForm(FlaskForm):
    # LoginForm definition here
    pass

class RegistrationForm(FlaskForm):
    # RegistrationForm definition here
    pass

class RecoverPasswordForm(FlaskForm):
    # RecoverPasswordForm definition here
    pass

class ResetPasswordForm(FlaskForm):
    # ResetPasswordForm definition here
    pass

class EditProfileForm(FlaskForm):
    # EditProfileForm definition here
    pass

class BlockForm(FlaskForm):
    # BlockForm definition here
    pass

class GroupForm(FlaskForm):
    # GroupForm definition here
    pass

class SendMessageForm(FlaskForm):
    # SendMessageForm definition here
    pass

class PostStatusForm(FlaskForm):
    # PostStatusForm definition here
    pass
