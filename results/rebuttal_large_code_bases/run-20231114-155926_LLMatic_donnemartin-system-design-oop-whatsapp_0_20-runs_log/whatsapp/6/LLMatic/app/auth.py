from flask import Blueprint, request, session, url_for, render_template
from werkzeug.utils import redirect
from app.models import User
from app import db

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/signup', methods=['POST'])
def signup_post():
	username = request.form.get('username')
	password = request.form.get('password')
	
	user = db.session.query(User).filter(User.username == username).first()
	
	if user:
		return 'Username already exists'
	
	new_user = User(id=None, email=username, password='', profile_picture='', status_message='', privacy_settings='', blocked_contacts=[])
	new_user.set_password(password)
	db.session.add(new_user)
	db.session.commit()
	
	return redirect(url_for('main.index'))

@auth.route('/login', methods=['POST'])
def login_post():
	username = request.form.get('username')
	password = request.form.get('password')
	
	user = db.session.query(User).filter(User.username == username).first()
	
	if not user or not user.check_password(password):
		return 'Could not login. Please check and try again.'
	
	session['user_id'] = user.id
	
	return 'You are now logged in'

@auth.route('/logout')
def logout():
	session.pop('user_id', None)
	return 'You are now logged out'

@auth.route('/recover', methods=['GET', 'POST'])
def recover():
	if request.method == 'POST':
		username = request.form.get('username')
		
		user = db.session.query(User).filter(User.username == username).first()
		
		if not user:
			return 'Could not find user. Please check and try again.'
		
		# Generate a password reset token and send it to the user's email address
		reset_token = user.get_reset_password_token(secret_key='secret_key')
		# Here we should send the reset_token to the user's email address
		# For the purpose of this task, we will just print it
		print(f'Reset token: {reset_token}')
		
		return 'Password recovery email has been sent.'
	
	return render_template('recover.html')
