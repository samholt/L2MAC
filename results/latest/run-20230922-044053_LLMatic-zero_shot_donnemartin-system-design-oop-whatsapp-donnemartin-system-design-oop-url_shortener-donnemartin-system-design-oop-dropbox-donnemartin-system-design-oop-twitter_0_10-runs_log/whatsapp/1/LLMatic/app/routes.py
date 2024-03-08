from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.models import User, Contact, Message, Group, GroupMessage, Status
from app.forms import LoginForm, RegistrationForm, MessageForm, GroupForm, StatusForm

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid email or password')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		return redirect(url_for('home'))
	return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you are now a registered user!')
		return redirect(url_for('login'))
	return render_template('register.html', form=form)

@app.route('/chat/<contact_id>', methods=['GET', 'POST'])
@login_required
def chat(contact_id):
	form = MessageForm()
	if form.validate_on_submit():
		message = Message(sender_id=current_user.id, receiver_id=contact_id, text=form.text.data)
		db.session.add(message)
		db.session.commit()
		return redirect(url_for('chat', contact_id=contact_id))
	messages = Message.query.filter_by(sender_id=current_user.id, receiver_id=contact_id).all()
	return render_template('chat.html', form=form, messages=messages)

@app.route('/group_chat/<group_id>', methods=['GET', 'POST'])
@login_required
def group_chat(group_id):
	form = MessageForm()
	if form.validate_on_submit():
		message = GroupMessage(sender_id=current_user.id, group_id=group_id, text=form.text.data)
		db.session.add(message)
		db.session.commit()
		return redirect(url_for('group_chat', group_id=group_id))
	messages = GroupMessage.query.filter_by(group_id=group_id).all()
	return render_template('group_chat.html', form=form, messages=messages)

@app.route('/status', methods=['GET', 'POST'])
@login_required
def status():
	form = StatusForm()
	if form.validate_on_submit():
		status = Status(user_id=current_user.id, image=form.image.data, visibility=form.visibility.data)
		db.session.add(status)
		db.session.commit()
		return redirect(url_for('status'))
	statuses = Status.query.filter_by(user_id=current_user.id).all()
	return render_template('status.html', form=form, statuses=statuses)
