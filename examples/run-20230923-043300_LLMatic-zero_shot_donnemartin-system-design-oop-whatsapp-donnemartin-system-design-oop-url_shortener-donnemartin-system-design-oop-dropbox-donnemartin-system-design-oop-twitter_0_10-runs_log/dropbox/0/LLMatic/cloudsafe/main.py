from flask import Flask
from cloudsafe.controllers.user_controller import user_controller
from cloudsafe.controllers.file_controller import file_controller
from cloudsafe.controllers.folder_controller import folder_controller
from cloudsafe.controllers.shared_link_controller import shared_link_controller
from cloudsafe.controllers.shared_folder_controller import shared_folder_controller

app = Flask(__name__)
app.register_blueprint(user_controller)
app.register_blueprint(file_controller)
app.register_blueprint(folder_controller)
app.register_blueprint(shared_link_controller)
app.register_blueprint(shared_folder_controller)

if __name__ == '__main__':
	app.run(debug=True)
