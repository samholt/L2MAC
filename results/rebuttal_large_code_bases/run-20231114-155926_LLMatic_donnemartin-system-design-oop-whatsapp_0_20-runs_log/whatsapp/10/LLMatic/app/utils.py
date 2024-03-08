import os
import uuid
from PIL import Image
from flask import current_app
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer


def generate_unique_filename(original_filename):
	"""Generate a unique filename based on the original filename."""
	base_name, extension = os.path.splitext(original_filename)
	unique_id = uuid.uuid4()
	new_filename = f'{base_name}_{unique_id}{extension}'
	return new_filename


def resize_image(image_file, size):
	"""Resize an image to the specified size."""
	image = Image.open(image_file)
	resized_image = image.resize(size)
	resized_image_file = generate_unique_filename(image_file)
	resized_image.save(resized_image_file)
	return resized_image_file


def send_email(to, subject, body):
	"""Send an email."""
	msg = Message(subject,
				  sender=current_app.config['MAIL_USERNAME'],
				  recipients=[to])
	msg.body = body
	current_app.mail.send(msg)


def generate_recovery_token(email):
	"""Generate a unique token for password recovery."""
	serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
	return serializer.dumps(email, salt=current_app.config['SECURITY_PASSWORD_SALT'])

