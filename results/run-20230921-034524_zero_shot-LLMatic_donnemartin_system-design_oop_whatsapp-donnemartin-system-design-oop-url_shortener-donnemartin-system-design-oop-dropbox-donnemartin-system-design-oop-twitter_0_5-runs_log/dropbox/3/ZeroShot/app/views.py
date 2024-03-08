from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from app.models import User, File, SharedFile


@app.route('/')
@login_required
def home():
	files = File.query.filter_by(user_id=current_user.id).all()
	shared_files = SharedFile.query.filter_by(user_id=current_user.id).all()
	return render_template('home.html', files=files, shared_files=shared_files)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		user = User.query.filter_by(username=request.form['username']).first()
		if user and user.password == request.form['password']:
			login_user(user)
			return redirect(url_for('home'))
	return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))


@app.route('/upload', methods=['POST'])
@login_required
def upload():
	file = File(user_id=current_user.id, filename=request.files['file'].filename, content=request.files['file'].read())
	db.session.add(file)
	db.session.commit()
	return redirect(url_for('home'))


@app.route('/download/<int:file_id>')
@login_required
def download(file_id):
	file = File.query.get(file_id)
	if file.user_id != current_user.id and not SharedFile.query.filter_by(file_id=file_id, user_id=current_user.id).first():
		abort(403)
	response = make_response(file.content)
	response.headers.set('Content-Type', 'application/octet-stream')
	response.headers.set('Content-Disposition', 'attachment', filename=file.filename)
	return response


@app.route('/share/<int:file_id>', methods=['POST'])
@login_required
def share(file_id):
	user = User.query.filter_by(username=request.form['username']).first()
	if not user:
		abort(404)
	shared_file = SharedFile(file_id=file_id, user_id=user.id)
	db.session.add(shared_file)
	db.session.commit()
	return redirect(url_for('home'))
