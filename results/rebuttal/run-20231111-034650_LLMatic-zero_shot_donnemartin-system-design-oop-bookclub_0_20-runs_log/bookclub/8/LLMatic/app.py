from flask import Flask, render_template, request, redirect, url_for, flash
from models import User, BookClub, Meeting

app = Flask(__name__)
app.secret_key = 'secret'

users = {}
book_clubs = {}

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		username = request.form['username']
		email = request.form['email']
		password = request.form['password']
		if email not in users:
			users[email] = User(username, email, password)
			flash('Registration successful!')
			return redirect(url_for('login'))
		else:
			flash('User already exists!')
	return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		if email in users and users[email].password == password:
			flash('Login successful!')
			return redirect(url_for('hello_world'))
		else:
			flash('Invalid credentials!')
	return render_template('login.html')

@app.route('/logout')
def logout():
	flash('You have been logged out.')
	return redirect(url_for('login'))

@app.route('/create_book_club', methods=['GET', 'POST'])
def create_book_club():
	if request.method == 'POST':
		name = request.form['name']
		description = request.form['description']
		is_private = request.form['is_private']
		admin = request.form['admin']
		if name not in book_clubs:
			book_clubs[name] = BookClub(name, description, is_private, admin)
			flash('Book club created successfully!')
			return redirect(url_for('view_book_club', name=name))
		else:
			flash('Book club already exists!')
	return render_template('create_book_club.html')

@app.route('/view_book_club/<name>')
def view_book_club(name):
	if name in book_clubs:
		return render_template('view_book_club.html', book_club=book_clubs[name])
	else:
		flash('Book club does not exist!')
		return redirect(url_for('create_book_club'))

@app.route('/edit_book_club/<name>', methods=['GET', 'POST'])
def edit_book_club(name):
	if request.method == 'POST':
		new_name = request.form['new_name']
		description = request.form['description']
		is_private = request.form['is_private']
		if name in book_clubs:
			book_club = book_clubs[name]
			book_club.name = new_name
			book_club.description = description
			book_club.is_private = is_private
			book_clubs[new_name] = book_club
			if new_name != name:
				del book_clubs[name]
			flash('Book club updated successfully!')
			return redirect(url_for('view_book_club', name=new_name))
		else:
			flash('Book club does not exist!')
		return redirect(url_for('create_book_club'))
	else:
		if name in book_clubs:
			return render_template('edit_book_club.html', book_club=book_clubs[name])
		else:
			flash('Book club does not exist!')
			return redirect(url_for('create_book_club'))

@app.route('/delete_book_club/<name>')
def delete_book_club(name):
	if name in book_clubs:
		del book_clubs[name]
		flash('Book club deleted successfully!')
	else:
		flash('Book club does not exist!')
	return redirect(url_for('create_book_club'))

@app.route('/join_book_club/<name>', methods=['GET', 'POST'])
def join_book_club(name):
	if request.method == 'POST':
		email = request.form['email']
		if name in book_clubs and email in users:
			book_club = book_clubs[name]
			user = users[email]
			if not book_club.is_private:
				book_club.members.append(user)
				flash('You have joined the book club!')
				return redirect(url_for('view_book_club', name=name))
			else:
				flash('This is a private book club. Request sent to admin.')
				return redirect(url_for('request_join_book_club', name=name, email=email))
		else:
			flash('Book club or user does not exist!')
			return redirect(url_for('create_book_club'))
	else:
		if name in book_clubs:
			return render_template('join_book_club.html', book_club=book_clubs[name])
		else:
			flash('Book club does not exist!')
			return redirect(url_for('create_book_club'))

@app.route('/request_join_book_club/<name>/<email>')
def request_join_book_club(name, email):
	if name in book_clubs and email in users:
		book_club = book_clubs[name]
		user = users[email]
		book_club.admin.notifications.append(f'{user.username} wants to join your book club.')
		flash('Request sent to book club admin.')
	else:
		flash('Book club or user does not exist!')
	return redirect(url_for('create_book_club'))

@app.route('/manage_requests/<name>', methods=['GET', 'POST'])
def manage_requests(name):
	if request.method == 'POST':
		request_id = request.form['request_id']
		action = request.form['action']
		if name in book_clubs:
			book_club = book_clubs[name]
			if request_id < len(book_club.admin.notifications):
				if action == 'accept':
					user = users[book_club.admin.notifications[request_id].split(' ')[0]]
					book_club.members.append(user)
					book_club.admin.notifications.pop(request_id)
					flash('Request accepted.')
				elif action == 'reject':
					book_club.admin.notifications.pop(request_id)
					flash('Request rejected.')
			else:
				flash('Invalid request id.')
			return redirect(url_for('manage_requests', name=name))
		else:
			flash('Book club does not exist!')
			return redirect(url_for('create_book_club'))
	else:
		if name in book_clubs:
			return render_template('manage_requests.html', book_club=book_clubs[name])
		else:
			flash('Book club does not exist!')
			return redirect(url_for('create_book_club'))

@app.route('/schedule_meeting/<name>', methods=['GET', 'POST'])
def schedule_meeting(name):
	if request.method == 'POST':
		date = request.form['date']
		time = request.form['time']
		book = request.form['book']
		if name in book_clubs:
			book_club = book_clubs[name]
			meeting = Meeting(date, time, book, book_club)
			book_club.meetings.append(meeting)
			flash('Meeting scheduled successfully!')
			return redirect(url_for('view_book_club', name=name))
		else:
			flash('Book club does not exist!')
		return redirect(url_for('create_book_club'))
	else:
		if name in book_clubs:
			return render_template('schedule_meeting.html', book_club=book_clubs[name])
		else:
			flash('Book club does not exist!')
			return redirect(url_for('create_book_club'))

@app.route('/upcoming_meetings/<name>')
def upcoming_meetings(name):
	if name in book_clubs:
		return render_template('upcoming_meetings.html', book_club=book_clubs[name])
	else:
		flash('Book club does not exist!')
		return redirect(url_for('create_book_club'))

@app.route('/send_reminders/<name>')
def send_reminders(name):
	if name in book_clubs:
		book_club = book_clubs[name]
		for member in book_club.members:
			member.notifications.append('Reminder: Upcoming meeting in ' + name)
		flash('Meeting reminders sent successfully!')
		return redirect(url_for('view_book_club', name=name))
	else:
		flash('Book club does not exist!')
		return redirect(url_for('create_book_club'))

if __name__ == '__main__':
	app.run()
