import sqlite3
from models.group import Group, GroupMember
from models.status import Status

class Database:
	def __init__(self):
		self.conn = sqlite3.connect('chat.db')
		self.cursor = self.conn.cursor()
		self.create_tables()

	def create_tables(self):
		self.cursor.execute('CREATE TABLE IF NOT EXISTS groups (id INTEGER PRIMARY KEY, name TEXT, picture TEXT, admin_id INTEGER)')
		self.cursor.execute('CREATE TABLE IF NOT EXISTS group_members (group_id INTEGER, user_id INTEGER)')
		self.cursor.execute('CREATE TABLE IF NOT EXISTS statuses (user_id INTEGER, image TEXT, visibility TEXT, timestamp DATETIME)')
		self.conn.commit()

	def save_group(self, group):
		if group.id is None:
			self.cursor.execute('INSERT INTO groups (name, picture, admin_id) VALUES (?, ?, ?)', (group.name, group.picture, group.admin_id))
			group.id = self.cursor.lastrowid
		else:
			self.cursor.execute('UPDATE groups SET name = ?, picture = ?, admin_id = ? WHERE id = ?', (group.name, group.picture, group.admin_id, group.id))
		self.conn.commit()
		return group.id

	def get_group(self, group_id):
		self.cursor.execute('SELECT * FROM groups WHERE id = ?', (group_id,))
		row = self.cursor.fetchone()
		return Group(row[0], row[1], row[2], row[3]) if row else None

	def save_group_member(self, group_member):
		self.cursor.execute('INSERT INTO group_members (group_id, user_id) VALUES (?, ?)', (group_member.group_id, group_member.user_id))
		self.conn.commit()

	def delete_group_member(self, group_id, user_id):
		self.cursor.execute('DELETE FROM group_members WHERE group_id = ? AND user_id = ?', (group_id, user_id))
		self.conn.commit()

	def save_status(self, status):
		self.cursor.execute('INSERT INTO statuses (user_id, image, visibility, timestamp) VALUES (?, ?, ?, ?)', (status.user_id, status.image, status.visibility, status.timestamp))
		self.conn.commit()

	def get_status(self, user_id):
		self.cursor.execute('SELECT * FROM statuses WHERE user_id = ?', (user_id,))
		row = self.cursor.fetchone()
		return Status(row[0], row[1], row[2], row[3]) if row else None

	def update_status(self, status):
		self.cursor.execute('UPDATE statuses SET visibility = ? WHERE user_id = ?', (status.visibility, status.user_id))
		self.conn.commit()
