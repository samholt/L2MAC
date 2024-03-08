from flask import render_template, request, redirect, url_for
from cloudsafe.controllers.folder_controller import folder_controller

class FolderView:
	def __init__(self):
		self.controller = folder_controller

	def create(self):
		if request.method == 'POST':
			name = request.form['name']
			self.controller.create(name)
			return redirect(url_for('dashboard'))
		return render_template('create_folder.html')

	def delete(self, folder_id):
		self.controller.delete(folder_id)
		return redirect(url_for('dashboard'))
