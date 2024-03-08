import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


class User:
	def __init__(self, id, name, email, password, profile_picture, storage_used):
		self.id = id
		self.name = name
		self.email = email
		self.password = generate_password_hash(password)
		self.profile_picture = profile_picture
		self.storage_used = storage_used

	@staticmethod
	def register(name, email, password, profile_picture):
		# Connect to the database
		conn = sqlite3.connect('cloudsafe.db')
		c = conn.cursor()

		# Insert the new user into the database
		c.execute("""INSERT INTO users (name, email, password, profile_picture, storage_used) VALUES (?, ?, ?, ?, ?)""",
				  (name, email, generate_password_hash(password), profile_picture, 0))

		# Commit the changes and close the connection
		conn.commit()
		conn.close()

	@staticmethod
	def authenticate(email, password):
		# Connect to the database
		conn = sqlite3.connect('cloudsafe.db')
		c = conn.cursor()

		# Retrieve the user with the given email
		c.execute("""SELECT * FROM users WHERE email = ?""", (email,))
		user = c.fetchone()

		# If the user exists and the password is correct, return the user
		if user and check_password_hash(user[3], password):
			return User(*user)

		# If the user does not exist or the password is incorrect, return None
		return None

	def update_profile(self, name, email, password, profile_picture):
		# Connect to the database
		conn = sqlite3.connect('cloudsafe.db')
		c = conn.cursor()

		# Update the user's profile in the database
		c.execute("""UPDATE users SET name = ?, email = ?, password = ?, profile_picture = ? WHERE id = ?""",
				  (name, email, generate_password_hash(password), profile_picture, self.id))

		# Commit the changes and close the connection
		conn.commit()
		conn.close()

	def calculate_storage_used(self):
		# Connect to the database
		conn = sqlite3.connect('cloudsafe.db')
		c = conn.cursor()

		# Calculate the total size of the user's files
		c.execute("""SELECT SUM(size) FROM files WHERE user_id = ?""", (self.id,))
		storage_used = c.fetchone()[0]

		# Update the user's storage used in the database
		c.execute("""UPDATE users SET storage_used = ? WHERE id = ?""", (storage_used, self.id))

		# Commit the changes and close the connection
		conn.commit()
		conn.close()

		# Update the storage used attribute
		self.storage_used = storage_used
