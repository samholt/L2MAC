"""
This file runs the application.
"""

from app import create_app

app, socketio = create_app('default')

if __name__ == '__main__':
    socketio.run(app)
