# pylint: skip-file
# pytype: skip-file
from setuptools import find_packages, setup

setup(
    name="url_shortener",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask==2.0.2",
        "requests==2.26.0",
        "pytest==6.2.5",
        "Flask-Session==0.4.0",
    ],
    entry_points={
        "console_scripts": [
            "url-shortener=app:app.run",
        ],
    },
)
