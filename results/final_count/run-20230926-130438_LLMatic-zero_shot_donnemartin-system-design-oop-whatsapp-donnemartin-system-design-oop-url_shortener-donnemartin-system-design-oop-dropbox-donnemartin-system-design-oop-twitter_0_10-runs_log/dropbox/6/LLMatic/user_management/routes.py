from flask import Blueprint, request, render_template, session
from .models import User

user_management = Blueprint('user_management', __name__)

mock_db = {}

@user_management.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		name = request.form.get('name')
		email = request.form.get('email')
		password = request.form.get('password')
		user = User(name, email, password)
		mock_db[email] = user
		return 'Registration successful'
	return render_template('register.html')

@user_management.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		user = mock_db.get(email)
		if user and user.password == password:
			session['user'] = user.email
			return 'Login successful'
		return 'Invalid credentials'
	return render_template('login.html')

@user_management.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
	if request.method == 'POST':
		email = request.form.get('email')
		user = mock_db.get(email)
		if user:
			new_password = 'new_password'
			user.password = new_password
			return 'Password reset successful. Your new password is: ' + new_password
		return 'Email not found'
	return render_template('forgot_password.html')

@user_management.route('/profile', methods=['GET', 'POST'])
def profile():
	if 'user' in session:
		user = mock_db.get(session['user'])
		if request.method == 'POST':
			new_password = request.form.get('new_password')
			user.password = new_password
			return 'Password changed successfully'
		return render_template('profile.html', user=user)
	return 'Please login to view this page'
