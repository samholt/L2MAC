from flask import render_template, request, redirect, url_for
from cloudsafe.controllers.shared_folder_controller import shared_folder_controller

class SharedFolderView:
	def __init__(self):
		self.controller = shared_folder_controller

	def create(self, folder_id):
		folder = self.controller.create(folder_id)
		return render_template('shared_folder.html', folder=folder)

	def delete(self, folder_id):
		self.controller.delete(folder_id)
		return redirect(url_for('dashboard'))

