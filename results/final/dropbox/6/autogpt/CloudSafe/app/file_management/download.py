from .file import File


def download_file(file_id):
    # TODO: Retrieve the file from the storage system using the file_id
    file = None
    if file:
        return file.content
    else:
        return None


def download_files_as_zip(file_ids):
    # TODO: Retrieve the files from the storage system using the file_ids
    files = []
    # TODO: Create a ZIP archive containing the files
    zip_content = ''
    return zip_content