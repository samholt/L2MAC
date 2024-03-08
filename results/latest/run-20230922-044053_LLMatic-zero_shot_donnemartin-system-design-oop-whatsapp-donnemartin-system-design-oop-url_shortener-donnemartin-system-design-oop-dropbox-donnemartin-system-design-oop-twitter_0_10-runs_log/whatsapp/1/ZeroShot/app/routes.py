from flask import render_template, flash, redirect, url_for, request
from app import app, db, login
from app.forms import LoginForm, RegistrationForm, EditProfileForm, MessageForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Message
from datetime import datetime


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
	form = MessageForm()
	if form.validate_on_submit():
		msg = Message(body=form.message.data, author=current_user)
		db.session.add(msg)
		db.session.commit()
		flash('Your message is now live!')
		return redirect(url_for('index'))
	messages = current_user.messages_received.order_by(Message.timestamp.desc())
	return render_template('index.html', title='Home', form=form, messages=messages)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid email or password')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(next_page)
	return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you are now a registered user!')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)


@app.route('/user/<email>')
@login_required
def user(email):
	user = User.query.filter_by(email=email).first_or_404()
	messages = user.messages_received.order_by(Message.timestamp.desc())
	return render_template('user.html', user=user, messages=messages)


@app.before_request
def before_request():
	if current_user.is_authenticated:
		current_user.last_seen = datetime.utcnow()
		db.session.commit()


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
	form = EditProfileForm(current_user.email)
	if form.validate_on_submit():
		current_user.email = form.email.data
		current_user.about_me = form.about_me.data
		db.session.commit()
		flash('Your changes have been saved.')
		return redirect(url_for('edit_profile'))
	elif request.method == 'GET':
		form.email.data = current_user.email
		form.about_me.data = current_user.about_me
	return render_template('edit_profile.html', title='Edit Profile', form=form)
