from flask import Flask, request, jsonify, redirect
import datetime
from models import User, URL, db

app = Flask(__name__)

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	url = URL(original_url=data['original_url'], shortened_url=data['shortened_url'], user_id=data['user_id'], expiration_date=data['expiration_date'])
	db[url.shortened_url] = url
	return jsonify(url.to_dict()), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = db.get(short_url)
	if url and url.expiration_date > datetime.datetime.now():
		return redirect(url.original_url, code=302)
	else:
		return 'URL not found or expired', 404

@app.route('/user/<user_id>', methods=['GET'])
def user_dashboard(user_id):
	user = db.get(user_id)
	if user:
		return jsonify([url.to_dict() for url in user.urls])
	else:
		return 'User not found', 404

@app.route('/admin', methods=['GET'])
def admin_dashboard():
	users = [user.to_dict() for user in db.values() if isinstance(user, User)]
	urls = [url.to_dict() for url in db.values() if isinstance(url, URL)]
	return jsonify({'users': users, 'urls': urls})

if __name__ == '__main__':
	app.run(debug=True)
