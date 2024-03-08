from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt, socketio
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm, MessageForm
from app.models import User, Message
from flask_login import login_user, current_user, logout_user, login_required
from flask_socketio import send, join_room, leave_room

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', title='Home')

@app.route("/register", methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Your account has been created! You are now able to log in', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')
	return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		if form.picture.data:
			current_user.image_file = save_picture(form.picture.data)
		current_user.email = form.email.data
		db.session.commit()
		flash('Your account has been updated!', 'success')
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.email.data = current_user.email
	image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
	return render_template('account.html', title='Account', image_file=image_file, form=form)

@app.route("/chat", methods=['GET', 'POST'])
@login_required
def chat():
	form = MessageForm()
	if form.validate_on_submit():
		msg = Message(content=form.content.data, author=current_user)
		db.session.add(msg)
		db.session.commit()
		flash('Your message has been sent!', 'success')
		return redirect(url_for('chat'))
	messages = Message.query.order_by(Message.date_posted.desc()).all()
	return render_template('chat.html', title='Chat', form=form, messages=messages)

@socketio.on('message')
def handleMessage(msg):
	send(msg, broadcast=True)

@socketio.on('join')
def on_join(data):
	username = data['username']
	room = data['room']
	join_room(room)
	send(username + ' has entered the room.', room=room)

@socketio.on('leave')
def on_leave(data):
	username = data['username']
	room = data['room']
	leave_room(room)
	send(username + ' has left the room.', room=room)
