from flask import Flask, request

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'book_clubs': {},
	'meetings': {},
	'discussions': {},
	'book_selections': {},
	'user_profiles': {},
	'recommendations': {},
	'admin_actions': {},
	'notifications': {},
	'resources': {}
}


# User class
class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.profile = {'username': username, 'following': [], 'books': []}

	def create(self):
		DATABASE['users'][self.username] = self
		DATABASE['user_profiles'][self.username] = self.profile

	def update_profile(self, profile_updates):
		self.profile.update(profile_updates)
		DATABASE['user_profiles'][self.username] = self.profile

	def list_books(self):
		return self.profile['books']

	def follow_user(self, user_to_follow):
		self.profile['following'].append(user_to_follow)
		DATABASE['user_profiles'][self.username] = self.profile

	def generate_recommendations(self):
		# Mock recommendation engine
		# In a real-world scenario, this would be a complex algorithm
		# For simplicity, we'll recommend the most popular books that the user hasn't read yet
		all_books = set(book for user in DATABASE['user_profiles'].values() for book in user['books'])
		user_books = set(self.profile['books'])
		recommendations = list(all_books - user_books)
		DATABASE['recommendations'][self.username] = recommendations
		return recommendations

	@staticmethod
	def login(username, password):
		return DATABASE['users'].get(username).password == password

	@staticmethod
	def get_profile(username):
		return DATABASE['user_profiles'].get(username)

	@staticmethod
	def get_recommendations(username):
		return DATABASE['recommendations'].get(username)


# Admin class
class Admin(User):
	def __init__(self, username, password):
		super().__init__(username, password)

	def manage_user_account(self, username, action):
		# Mock actions: 'activate', 'deactivate', 'delete'
		DATABASE['admin_actions'][username] = action

	def manage_book_club(self, book_club_name, action):
		# Mock actions: 'create', 'delete'
		DATABASE['admin_actions'][book_club_name] = action

	def remove_inappropriate_content(self, content_id):
		# Mock content removal
		DATABASE['resources'].pop(content_id, None)

	def view_analytics(self):
		# Mock analytics
		return {'users': len(DATABASE['users']), 'book_clubs': len(DATABASE['book_clubs'])}

	def send_notification(self, username, notification):
		# Mock notification sending
		DATABASE['notifications'][username] = notification

	def send_email_alert(self, email, alert):
		# Mock email alert sending
		# In a real-world scenario, this would send an email
		DATABASE['notifications'][email] = alert


@app.route('/get_profile', methods=['GET'])
def get_profile():
	username = request.args.get('username')
	profile = User.get_profile(username)
	if profile:
		return profile, 200
	else:
		return 'User not found', 404


@app.route('/update_profile', methods=['POST'])
def update_profile():
	data = request.get_json()
	user = DATABASE['users'].get(data['username'])
	if user:
		user.update_profile(data['profile_updates'])
		return 'Profile updated successfully', 200
	else:
		return 'User not found', 404


@app.route('/follow_user', methods=['POST'])
def follow_user():
	data = request.get_json()
	user = DATABASE['users'].get(data['username'])
	if user:
		user.follow_user(data['user_to_follow'])
		return 'User followed successfully', 200
	else:
		return 'User not found', 404


@app.route('/generate_recommendations', methods=['POST'])
def generate_recommendations():
	data = request.get_json()
	user = DATABASE['users'].get(data['username'])
	if user:
		recommendations = user.generate_recommendations()
		return {'recommendations': recommendations}, 200
	else:
		return 'User not found', 404


@app.route('/get_recommendations', methods=['GET'])
def get_recommendations():
	username = request.args.get('username')
	recommendations = User.get_recommendations(username)
	if recommendations is not None:
		return {'recommendations': recommendations}, 200
	else:
		return 'No recommendations found', 404


@app.route('/share_resource', methods=['POST'])
def share_resource():
	data = request.get_json()
	DATABASE['resources'][data['resource_id']] = data['resource_content']
	return 'Resource shared successfully', 200


@app.route('/view_resource', methods=['GET'])
def view_resource():
	resource_id = request.args.get('resource_id')
	resource = DATABASE['resources'].get(resource_id)
	if resource is not None:
		return {'resource': resource}, 200
	else:
		return 'Resource not found', 404


if __name__ == '__main__':
	app.run(debug=True)
