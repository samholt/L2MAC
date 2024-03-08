import os


class FileUpload:
    def __init__(self, user):
        self.user = user
        self.allowed_file_types = ['.txt', '.pdf', '.png', '.jpg', '.jpeg', '.gif']
        self.max_file_size = 10 * 1024 * 1024  # 10 MB

    def upload_file(self, file):
        # Check file type and size
        # Save file securely


if __name__ == '__main__':
    # Retrieve user data securely
    user = None  # Replace with retrieved user data
    file_upload = FileUpload(user)
    file = None  # Replace with file to be uploaded
    file_upload.upload_file(file)
    print('File uploaded successfully.')