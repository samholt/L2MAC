class Vendor:
	def __init__(self, id, name, reviews):
		self.id = id
		self.name = name
		self.reviews = reviews


vendors_db = {}


def add_vendor(id, name, reviews):
	vendors_db[id] = Vendor(id, name, reviews)


def get_vendor(id):
	return vendors_db.get(id, None)


def get_all_vendors():
	return list(vendors_db.values())


def delete_vendor(id):
	if id in vendors_db:
		del vendors_db[id]


def update_vendor(id, name=None, reviews=None):
	if id in vendors_db:
		if name is not None:
			vendors_db[id].name = name
		if reviews is not None:
			vendors_db[id].reviews = reviews
