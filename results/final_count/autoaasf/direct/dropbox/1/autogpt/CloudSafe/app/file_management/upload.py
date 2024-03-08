from .file import File


def upload_file(name, content, owner):
    new_file = File(name, content, owner)
    # TODO: Save the file to the storage system
    return new_file


def handle_drag_and_drop_upload(file_data, owner):
    # TODO: Process the file data from the drag and drop event
    name = ''  # Extract the file name from the file_data
    content = ''  # Extract the file content from the file_data
    return upload_file(name, content, owner)