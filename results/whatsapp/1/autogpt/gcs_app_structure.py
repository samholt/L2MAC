import os


def create_gcs_app_structure():
    os.makedirs('gcs_app', exist_ok=True)
    os.makedirs('gcs_app/auth', exist_ok=True)
    os.makedirs('gcs_app/profiles', exist_ok=True)
    os.makedirs('gcs_app/contacts', exist_ok=True)
    os.makedirs('gcs_app/messaging', exist_ok=True)
    os.makedirs('gcs_app/groups', exist_ok=True)
    os.makedirs('gcs_app/status', exist_ok=True)
    os.makedirs('gcs_app/web_app', exist_ok=True)
    os.makedirs('gcs_app/connectivity', exist_ok=True)
    os.makedirs('gcs_app/offline_mode', exist_ok=True)
    os.makedirs('gcs_app/tests', exist_ok=True)


if __name__ == '__main__':
    create_gcs_app_structure()