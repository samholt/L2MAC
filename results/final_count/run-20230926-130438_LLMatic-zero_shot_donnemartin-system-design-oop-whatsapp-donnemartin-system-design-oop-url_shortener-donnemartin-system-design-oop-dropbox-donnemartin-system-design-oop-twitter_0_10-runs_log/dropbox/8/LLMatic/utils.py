import datetime
from typing import List

# Mock database
activity_log = []


class ActivityLogEntry:
	def __init__(self, user, action):
		self.user = user
		self.action = action
		self.timestamp = datetime.datetime.now()


def log_activity(user, action):
	entry = ActivityLogEntry(user, action)
	activity_log.append(entry)


def encrypt(file):
	# Placeholder encryption, replace with actual encryption algorithm
	file.content = file.content[::-1]
	return file


def decrypt(file):
	# Placeholder decryption, replace with actual decryption algorithm
	file.content = file.content[::-1]
	return file
