import sqlite3
from models.message import Message


def create_messages_table():
	with sqlite3.connect('gcs.db') as conn:
		cursor = conn.cursor()
		cursor.execute('CREATE TABLE IF NOT EXISTS messages (sender_id INTEGER, receiver_id INTEGER, text TEXT, read_status INTEGER, encryption_key TEXT)')

def send_message(sender_id: int, receiver_id: int, text: str, encryption_key: str) -> Message:
	create_messages_table()
	message = Message(sender_id=sender_id, receiver_id=receiver_id, text=text, read_status=False, encryption_key=encryption_key)
	with sqlite3.connect('gcs.db') as conn:
		cursor = conn.cursor()
		cursor.execute('INSERT INTO messages (sender_id, receiver_id, text, read_status, encryption_key) VALUES (?, ?, ?, ?, ?)', (message.sender_id, message.receiver_id, message.text, int(message.read_status), message.encryption_key))
	return message

def receive_message(sender_id: int, receiver_id: int) -> Message:
	with sqlite3.connect('gcs.db') as conn:
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM messages WHERE sender_id = ? AND receiver_id = ? ORDER BY rowid DESC LIMIT 1', (sender_id, receiver_id))
		message_data = cursor.fetchone()
		if message_data is None:
			return None
		return Message(sender_id=message_data[0], receiver_id=message_data[1], text=message_data[2], read_status=bool(message_data[3]), encryption_key=message_data[4])

def send_emoji(sender_id: int, receiver_id: int, emoji: str) -> Message:
	return send_message(sender_id, receiver_id, emoji, '')

def send_gif(sender_id: int, receiver_id: int, gif: str) -> Message:
	return send_message(sender_id, receiver_id, gif, '')

def send_sticker(sender_id: int, receiver_id: int, sticker: str) -> Message:
	return send_message(sender_id, receiver_id, sticker, '')
