class User:
	def __init__(self):
		self.users = {}

	def register(self, data):
		name = data.get('name')
		email = data.get('email')
		password = data.get('password')
		if not name or not email or not password:
			return {'status': 'error', 'message': 'Missing required fields'}
		if email in self.users:
			return {'status': 'error', 'message': 'User already exists'}
		self.users[email] = {'name': name, 'password': password}
		return {'status': 'success', 'message': 'User registered successfully'}

	def login(self, data):
		email = data.get('email')
		password = data.get('password')
		if not email or not password:
			return {'status': 'error', 'message': 'Missing required fields'}
		if email not in self.users or self.users[email]['password'] != password:
			return {'status': 'error', 'message': 'Invalid credentials'}
		return {'status': 'success', 'message': 'User logged in successfully'}
