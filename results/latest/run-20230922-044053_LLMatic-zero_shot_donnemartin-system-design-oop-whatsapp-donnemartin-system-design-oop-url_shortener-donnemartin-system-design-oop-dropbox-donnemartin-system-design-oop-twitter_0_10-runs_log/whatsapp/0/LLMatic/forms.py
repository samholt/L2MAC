from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from models import User


class RegistrationForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Register')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Please use a different email address.')


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Sign In')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError('Invalid email address.')


class ProfileForm(FlaskForm):
	profile_picture = FileField('Update Profile Picture')
	status_message = StringField('Status Message')
	privacy_settings = StringField('Privacy Settings')
	submit = SubmitField('Update')


class ContactForm(FlaskForm):
	contact_id = StringField('Contact ID', validators=[DataRequired()])
	blocked = BooleanField('Blocked')
	submit = SubmitField('Update')


class MessageForm(FlaskForm):
	recipient = StringField('Recipient', validators=[DataRequired()])
	text = StringField('Message', validators=[DataRequired()])
	submit = SubmitField('Send')
