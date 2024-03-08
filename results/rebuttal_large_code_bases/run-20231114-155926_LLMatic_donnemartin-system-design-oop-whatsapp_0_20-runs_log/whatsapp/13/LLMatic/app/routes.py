from flask import Blueprint, render_template, request, redirect, url_for
from .models import User, Group, DATABASE
from .app import db, app

bp = Blueprint('routes', __name__, url_prefix='/')

@app.route('/')
def index():
	return 'Hello, World!'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')
		user = User(id=len(DATABASE)+1, username=username, email='', password=password)
		DATABASE[user.id] = user
		return redirect(url_for('routes.login'))
	return 'Signup Page'

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')
		user = [user for user in DATABASE.values() if isinstance(user, User) and user.username == username and user.password == password]
		if user:
			return redirect(url_for('routes.index'))
	return 'Login Page'

@app.route('/set_online_status', methods=['POST'])
def set_online_status():
	user_id = int(request.form.get('user_id'))
	online_status = request.form.get('online_status') == 'True'
	user = DATABASE.get(user_id)
	if user:
		user.online = online_status
		DATABASE[user_id] = user
	return str(user)
