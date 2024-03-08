from app import app, db, socketio


if __name__ == '__main__':
	db.create_all()
	socketio.run(app)
