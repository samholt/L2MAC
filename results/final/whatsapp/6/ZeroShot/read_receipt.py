from datetime import datetime

class ReadReceipt:
	def __init__(self, reader):
		self.timestamp = datetime.now()
		self.reader = reader

	def to_dict(self):
		return {
			'timestamp': self.timestamp.isoformat(),
			'reader': self.reader.id
		}
