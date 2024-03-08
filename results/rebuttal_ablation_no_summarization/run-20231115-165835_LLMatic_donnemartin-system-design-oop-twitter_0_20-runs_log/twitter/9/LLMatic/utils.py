import os
import secrets
from PIL import Image
from flask import current_app

def save_profile_picture(form_picture):
	random_hex = secrets.token_hex(8)
	picture_fn = random_hex + '.jpg'
	picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
	output_size = (125, 125)
	i = Image.open(form_picture)
	i.thumbnail(output_size)
	i.save(picture_path)
	return picture_fn
