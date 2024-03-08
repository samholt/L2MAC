from flask import render_template, request, redirect, url_for
from cloudsafe.controllers.file_controller import file_controller


class FileView:
	def __init__(self):
		self.controller = file_controller

	def upload(self):
		if request.method == 'POST':
			file = request.files['file']
			self.controller.upload(file)
			return redirect(url_for('dashboard'))
		return render_template('upload.html')

	def download(self, file_id):
		file = self.controller.download(file_id)
		return file

	def delete(self, file_id):
		self.controller.delete(file_id)
		return redirect(url_for('dashboard'))
