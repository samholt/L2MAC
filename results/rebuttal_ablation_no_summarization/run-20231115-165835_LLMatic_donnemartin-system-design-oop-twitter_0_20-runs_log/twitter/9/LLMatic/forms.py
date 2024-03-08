from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, EqualTo

class RegistrationForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired()])
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Login')

class EditProfileForm(FlaskForm):
	profile_picture = StringField('Profile Picture')
	bio = TextAreaField('Bio')
	website_link = StringField('Website Link')
	location = StringField('Location')
	is_private = BooleanField('Private Profile')
	submit = SubmitField('Update Profile')
