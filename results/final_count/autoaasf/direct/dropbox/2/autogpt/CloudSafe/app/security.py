from cryptography.fernet import Fernet
import os


def generate_key():
    return Fernet.generate_key()


def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original_data = file.read()
    encrypted_data = fernet.encrypt(original_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)


def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    original_data = fernet.decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(original_data)


def secure_upload(file, key):
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    encrypt_file(file_path, key)
    return filename


def secure_download(filename, key):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    decrypt_file(file_path, key)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
