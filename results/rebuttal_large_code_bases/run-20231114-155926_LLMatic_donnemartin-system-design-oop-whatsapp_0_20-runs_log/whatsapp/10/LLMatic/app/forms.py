from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from app.models import User


class RegistrationForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Sign Up')

	def validate_email(self, email):
		user = User(id=0, email='', password='', profile_picture='', status_message='', privacy_settings='', last_seen='', contacts=[], blocked_contacts=[]).read()
		if user and user['email'] == email.data:
			raise ValidationError('Email already in use. Please choose a different one.')

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Log In')

class PasswordRecoveryForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired()])
	submit = SubmitField('Recover Password')

class ProfileForm(FlaskForm):
	profile_picture = FileField('Profile Picture')
	status_message = StringField('Status Message', validators=[DataRequired()])
	submit = SubmitField('Update Profile')

class PrivacyForm(FlaskForm):
	privacy_settings = StringField('Privacy Settings', validators=[DataRequired()])
	submit = SubmitField('Update Privacy Settings')

class ContactForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired()])
	submit = SubmitField('Add Contact')

class BlockForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired()])
	submit = SubmitField('Block Contact')

class GroupForm(FlaskForm):
	name = StringField('Group Name', validators=[DataRequired()])
	picture = FileField('Group Picture')
	participants = StringField('Participants', validators=[DataRequired()])
	submit = SubmitField('Create Group')

class AdminForm(FlaskForm):
	roles = StringField('Admin Roles', validators=[DataRequired()])
	permissions = StringField('Permissions', validators=[DataRequired()])
	submit = SubmitField('Assign Roles')

class MessageForm(FlaskForm):
	content = StringField('Content', validators=[DataRequired()])
	receiver = StringField('Receiver', validators=[DataRequired()])
	submit = SubmitField('Send Message')

class ImageForm(FlaskForm):
	image_file = FileField('Image File', validators=[DataRequired()])
	submit = SubmitField('Share Image')

class StatusForm(FlaskForm):
	image_file = FileField('Image File', validators=[DataRequired()])
	visibility = StringField('Visibility', validators=[DataRequired()])
	submit = SubmitField('Post Status')
