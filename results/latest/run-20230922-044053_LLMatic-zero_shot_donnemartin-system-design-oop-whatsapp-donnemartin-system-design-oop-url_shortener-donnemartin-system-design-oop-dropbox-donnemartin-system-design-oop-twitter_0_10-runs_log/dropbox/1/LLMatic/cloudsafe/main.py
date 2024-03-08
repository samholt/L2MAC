from flask import Flask
from cloudsafe.user.views import register, login, update_profile
from cloudsafe.file.views import upload, download, organize, versioning
from cloudsafe.share.views import generate_shareable_link, manage_shared_folder

app = Flask(__name__)

app.add_url_rule('/register', 'register', register, methods=['POST'])
app.add_url_rule('/login', 'login', login, methods=['POST'])
app.add_url_rule('/update_profile', 'update_profile', update_profile, methods=['PUT'])

app.add_url_rule('/upload', 'upload', upload, methods=['POST'])
app.add_url_rule('/download/<file_id>', 'download', download, methods=['GET'])
app.add_url_rule('/organize/<file_id>', 'organize', organize, methods=['PUT'])
app.add_url_rule('/versioning/<file_id>', 'versioning', versioning, methods=['PUT'])

app.add_url_rule('/generate_shareable_link', 'generate_shareable_link', generate_shareable_link, methods=['POST'])
app.add_url_rule('/manage_shared_folder', 'manage_shared_folder', manage_shared_folder, methods=['PUT'])

if __name__ == '__main__':
	app.run(debug=True)
