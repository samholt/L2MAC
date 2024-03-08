db = {'admins': {}}

def save_to_db(collection, id, data):
	if collection in db:
		db[collection][id] = data


def get_from_db(collection, id):
	if collection in db and id in db[collection]:
		return db[collection][id]
	return None
