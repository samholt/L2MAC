import random


def connectivity():
	return random.choice([True, False])


def restore_connectivity(queue, db):
	while queue:
		if connectivity():
			func, args = queue.pop(0)
			func(*args)
		else:
			break
	return db
