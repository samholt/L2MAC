from flask import render_template, url_for, flash, redirect, request, abort
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, UrlForm
from app.models import User, Url, Click
from flask_login import login_user, current_user, logout_user, login_required
import requests
import string
import random
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
def home():
	form = UrlForm()
	if form.validate_on_submit():
		original_url = form.original_url.data
		short_url = form.short_url.data
		expires_at = form.expires_at.data
		if not short_url:
			short_url = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))
		if not expires_at:
			expires_at = None
		else:
			expires_at = datetime.strptime(expires_at, '%Y-%m-%d %H:%M:%S')
		url = Url(original_url=original_url, short_url=short_url, creator=current_user, expires_at=expires_at)
		db.session.add(url)
		db.session.commit()
		flash('Your URL has been shortened!', 'success')
		return redirect(url_for('home'))
	return render_template('home.html', title='Home', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Your account has been created! You are now able to log in', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')
	return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
	return render_template('account.html', title='Account')

@app.route('/<short_url>')
def redirect_to_url(short_url):
	url = Url.query.filter_by(short_url=short_url).first()
	if url:
		url.clicks += 1
		click = Click(url=url, clicker_ip=request.remote_addr)
		db.session.add(click)
		db.session.commit()
		return redirect(url.original_url)
	else:
		abort(404)
