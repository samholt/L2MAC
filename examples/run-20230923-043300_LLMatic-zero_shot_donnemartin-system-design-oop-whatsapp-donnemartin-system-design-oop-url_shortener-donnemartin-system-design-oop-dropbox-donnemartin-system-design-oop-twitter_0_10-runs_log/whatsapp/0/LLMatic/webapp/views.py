from flask import render_template, request, redirect, url_for
from .forms import RegistrationForm, LoginForm, MessageForm, GroupForm, StatusForm, ProfileForm, ContactForm
from .app import app
from services import auth_service, user_service, message_service, group_service, status_service

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		auth_service.register(form.email.data, form.password.data)
		return redirect(url_for('login'))
	return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = auth_service.login(form.email.data, form.password.data)
		if user:
			return redirect(url_for('home'))
	return render_template('login.html', form=form)

@app.route('/profile', methods=['GET', 'POST'])
def profile():
	form = ProfileForm()
	if form.validate_on_submit():
		user_service.update_profile(form.profile_picture.data, form.status_message.data)
	return render_template('profile.html', form=form)

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
	form = ContactForm()
	if form.validate_on_submit():
		user_service.block_unblock_contact(form.contact.data)
	return render_template('contacts.html', form=form)

@app.route('/message', methods=['GET', 'POST'])
def message():
	form = MessageForm()
	if form.validate_on_submit():
		message_service.send_message(form.receiver.data, form.message.data)
	return render_template('message.html', form=form)

@app.route('/group', methods=['GET', 'POST'])
def group():
	form = GroupForm()
	if form.validate_on_submit():
		group_service.create_group(form.name.data, form.participants.data)
	return render_template('group.html', form=form)

@app.route('/status', methods=['GET', 'POST'])
def status():
	form = StatusForm()
	if form.validate_on_submit():
		status_service.post_status(form.image.data, form.visibility.data)
	return render_template('status.html', form=form)
