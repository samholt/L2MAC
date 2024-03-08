from flask import render_template, request, redirect, url_for
from cloudsafe.controllers.shared_link_controller import shared_link_controller

class SharedLinkView:
	def __init__(self):
		self.controller = shared_link_controller

	def create(self, file_id):
		link = self.controller.create(file_id)
		return render_template('shared_link.html', link=link)

	def delete(self, link_id):
		self.controller.delete(link_id)
		return redirect(url_for('dashboard'))

