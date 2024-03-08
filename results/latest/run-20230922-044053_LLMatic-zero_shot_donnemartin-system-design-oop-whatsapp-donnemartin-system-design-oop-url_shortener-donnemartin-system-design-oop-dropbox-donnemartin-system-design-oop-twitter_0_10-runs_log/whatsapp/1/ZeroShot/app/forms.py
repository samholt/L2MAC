from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Please use a different email address.')


class EditProfileForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
	submit = SubmitField('Submit')

	def __init__(self, original_email, *args, **kwargs):
		super(EditProfileForm, self).__init__(*args, **kwargs)
		self.original_email = original_email

	def validate_email(self, email):
		if email.data != self.original_email:
			user = User.query.filter_by(email=self.email.data).first()
			if user is not None:
				raise ValidationError('Please use a different email address.')


class MessageForm(FlaskForm):
	message = TextAreaField('Message', validators=[DataRequired(), Length(min=0, max=140)])
	submit = SubmitField('Submit')
