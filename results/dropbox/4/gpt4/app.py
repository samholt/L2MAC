from views.user_view import UserView
from views.file_view import FileView
from views.permission_view import PermissionView

if __name__ == '__main__':
	user_view = UserView()
	file_view = FileView()
	permission_view = PermissionView()

	# Here you can call the methods of the views to interact with the system
