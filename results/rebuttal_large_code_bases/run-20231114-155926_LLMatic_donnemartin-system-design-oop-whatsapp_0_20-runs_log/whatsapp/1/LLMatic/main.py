import os
from app import create_app, socketio

app = create_app()

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	while True:
		try:
			socketio.run(app, host='0.0.0.0', port=port)
			break
		except OSError as e:
			if 'Address already in use' in str(e):
				port += 1
				continue
			else:
				raise e
