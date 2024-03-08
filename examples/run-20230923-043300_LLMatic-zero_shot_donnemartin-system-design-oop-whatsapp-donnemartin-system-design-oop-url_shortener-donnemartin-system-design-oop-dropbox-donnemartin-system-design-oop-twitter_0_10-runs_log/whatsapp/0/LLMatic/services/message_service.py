import sqlite3

DB_NAME = 'chat.db'

class MessageService:
	@staticmethod
	def send_message(sender, receiver, message):
		conn = sqlite3.connect(DB_NAME)
		c = conn.cursor()
		c.execute('INSERT INTO messages (sender, receiver, message, read_receipt, encrypted) VALUES (?, ?, ?, ?, ?)', (sender, receiver, message, 0, 0))
		message_id = c.lastrowid
		conn.commit()
		conn.close()
		return {'id': message_id, 'sender': sender, 'receiver': receiver, 'message': message, 'read_receipt': 0, 'encrypted': 0}

	@staticmethod
	def queue_message(receiver, message):
		pass

	@staticmethod
	def send_queued_messages():
		pass
