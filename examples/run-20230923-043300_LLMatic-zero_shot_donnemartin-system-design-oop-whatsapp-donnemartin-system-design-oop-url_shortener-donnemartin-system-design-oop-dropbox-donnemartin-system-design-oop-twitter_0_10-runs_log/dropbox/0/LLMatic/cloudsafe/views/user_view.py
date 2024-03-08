from flask import render_template, request, redirect, url_for
from cloudsafe.controllers.user_controller import UserController


class UserView:
	def __init__(self):
		self.controller = UserController()

	def register(self):
		if request.method == 'POST':
			name = request.form['name']
			email = request.form['email']
			password = request.form['password']
			self.controller.register(name, email, password)
			return redirect(url_for('login'))
		return render_template('register.html')

	def login(self):
		if request.method == 'POST':
			email = request.form['email']
			password = request.form['password']
			user = self.controller.login(email, password)
			if user:
				return redirect(url_for('dashboard'))
			else:
				return 'Invalid credentials'
		return render_template('login.html')

	def profile(self):
		user = self.controller.get_current_user()
		return render_template('profile.html', user=user)
