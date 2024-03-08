from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegistrationForm(FlaskForm):
	email = StringField('Email')
	password = PasswordField('Password')
	submit = SubmitField('Register')

class LoginForm(FlaskForm):
	email = StringField('Email')
	password = PasswordField('Password')
	submit = SubmitField('Login')

class MessageForm(FlaskForm):
	receiver = StringField('Receiver')
	message = StringField('Message')
	submit = SubmitField('Send')

class GroupForm(FlaskForm):
	name = StringField('Name')
	participants = StringField('Participants')
	submit = SubmitField('Create')

class StatusForm(FlaskForm):
	image = StringField('Image')
	visibility = StringField('Visibility')
	submit = SubmitField('Post')

class ProfileForm(FlaskForm):
	profile_picture = StringField('Profile Picture')
	status_message = StringField('Status Message')
	submit = SubmitField('Update')

class ContactForm(FlaskForm):
	contact = StringField('Contact')
	submit = SubmitField('Block/Unblock')
