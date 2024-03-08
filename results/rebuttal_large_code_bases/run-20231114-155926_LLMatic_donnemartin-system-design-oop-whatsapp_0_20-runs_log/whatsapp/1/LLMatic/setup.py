from setuptools import setup, find_packages

setup(
    name='ChatApp',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-socketio',
        'flask-login',
        'flask-wtf',
        'flask-sqlalchemy',
        'flask-migrate',
        'eventlet'
    ],
    entry_points={
        'console_scripts': [
            'chatapp = main:main'
        ]
    }
)
