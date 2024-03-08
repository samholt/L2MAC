from flask import render_template, url_for, flash, redirect, request, session
from app import app, db
from app.models import User, Message, Group, Status
from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	# Route for user signup
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		# Validate input
		if not email or not password:
			flash('Invalid input!')
			return redirect(request.url)
		# Create new user
		user = User(email=email, password=generate_password_hash(password, method='sha256'))
		db.session.add(user)
		db.session.commit()
		flash('Account created!')
		return redirect(url_for('login'))
	return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	# Route for user login
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		# Validate input
		if not email or not password:
			flash('Invalid input!')
			return redirect(request.url)
		# Authenticate user
		user = User.query.filter_by(email=email).first()
		if user and check_password_hash(user.password, password):
			session['user_id'] = user.id
			flash('Logged in successfully!')
			return redirect(url_for('profile'))
		flash('Invalid email or password')
	return render_template('login.html')


@app.route('/logout')
def logout():
	# Route for user logout
	session.pop('user_id', None)
	flash('Logged out successfully!')
	return redirect(url_for('login'))


@app.route('/profile', methods=['GET', 'POST'])
def profile():
	# Route for user profile
	user = User.query.get(session['user_id'])
	if request.method == 'POST':
		# Update user profile
		user.email = request.form.get('email')
		user.password = generate_password_hash(request.form.get('password'), method='sha256')
		# Validate input
		if not user.email or not user.password:
			flash('Invalid input!')
			return redirect(request.url)
		db.session.commit()
		flash('Profile updated!')
	return render_template('profile.html', user=user)


@app.route('/chat', methods=['GET', 'POST'])
def chat():
	# Route for chat
	user = User.query.get(session['user_id'])
	if request.method == 'POST':
		# Send message
		receiver_email = request.form.get('receiver_email')
		message_content = request.form.get('message_content')
		# Validate input
		if not receiver_email or not message_content:
			flash('Invalid input!')
			return redirect(request.url)
		receiver = User.query.filter_by(email=receiver_email).first()
		if receiver:
			# Create new message
			message = Message(sender=user, recipient=receiver, content=message_content, read_receipt=False, encryption_key=Fernet.generate_key().decode())
			db.session.add(message)
			db.session.commit()
			flash('Message sent!')
		else:
			flash('User not found!')
	return render_template('chat.html', messages=user.sent_messages)


@app.route('/group', methods=['GET', 'POST'])
def group():
	# Route for group
	user = User.query.get(session['user_id'])
	if request.method == 'POST':
		# Create new group
		group_name = request.form.get('group_name')
		# Validate input
		if not group_name:
			flash('Invalid input!')
			return redirect(request.url)
		new_group = Group(name=group_name)
		new_group.set_admin(user)
		db.session.add(new_group)
		db.session.commit()
		flash('Group created!')
	return render_template('group.html', groups=user.admin_groups)


@app.route('/status', methods=['GET', 'POST'])
def status():
	# Route for status
	user = User.query.get(session['user_id'])
	if request.method == 'POST':
		# Post new status
		status_content = request.form.get('status_content')
		visibility = request.form.get('visibility')
		# Validate input
		if not status_content or not visibility:
			flash('Invalid input!')
			return redirect(request.url)
		new_status = Status(user=user, content=status_content, visibility=visibility)
		db.session.add(new_status)
		db.session.commit()
		flash('Status posted!')
	return render_template('status.html', statuses=user.statuses)


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
	# Route for contacts
	user = User.query.get(session['user_id'])
	if request.method == 'POST':
		# Add new contact
		contact_email = request.form.get('contact_email')
		# Validate input
		if not contact_email:
			flash('Invalid input!')
			return redirect(request.url)
		contact = User.query.filter_by(email=contact_email).first()
		if contact:
			user.contacts.append(contact)
			db.session.commit()
			flash('Contact added!')
		else:
			flash('User not found!')
	return render_template('contacts.html', contacts=user.contacts)
