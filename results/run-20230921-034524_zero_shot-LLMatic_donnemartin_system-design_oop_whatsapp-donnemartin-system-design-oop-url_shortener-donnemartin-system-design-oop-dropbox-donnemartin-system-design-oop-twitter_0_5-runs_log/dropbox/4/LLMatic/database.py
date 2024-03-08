import sqlite3

class Database:
	def __init__(self, db_name='file_storage.db'):
		self.conn = sqlite3.connect(db_name)
		self.cursor = self.conn.cursor()
		self.cursor.execute('CREATE TABLE IF NOT EXISTS files (id INTEGER PRIMARY KEY, name TEXT, size TEXT, type TEXT, content TEXT)')
		self.conn.commit()

	def create_record(self, table, record):
		self.start_transaction()
		try:
			columns = ', '.join(record.keys())
			placeholders = ', '.join('?' * len(record))
			self.cursor.execute(f"INSERT INTO {table} ({columns}) VALUES ({placeholders})", tuple(record.values()))
			self.conn.commit()
			self.commit_transaction()
		except:
			self.rollback_transaction()

	def read_record(self, table, record_id):
		self.cursor.execute(f"SELECT * FROM {table} WHERE id = ?", (record_id,))
		record = self.cursor.fetchone()
		if record is None:
			return None
		return {'name': record[1], 'size': record[2], 'type': record[3], 'content': record[4]}

	def update_record(self, table, record_id, record):
		self.start_transaction()
		try:
			columns = ', '.join(f'{key} = ?' for key in record.keys())
			self.cursor.execute(f"UPDATE {table} SET {columns} WHERE id = ?", tuple(record.values()) + (record_id,))
			self.conn.commit()
			self.commit_transaction()
		except:
			self.rollback_transaction()

	def delete_record(self, table, record_id):
		self.start_transaction()
		try:
			self.cursor.execute(f"DELETE FROM {table} WHERE id = ?", (record_id,))
			self.conn.commit()
			self.commit_transaction()
		except:
			self.rollback_transaction()

	def start_transaction(self):
		self.conn.execute('BEGIN TRANSACTION')

	def commit_transaction(self):
		self.conn.commit()

	def rollback_transaction(self):
		self.conn.rollback()

	def close(self):
		self.conn.close()
