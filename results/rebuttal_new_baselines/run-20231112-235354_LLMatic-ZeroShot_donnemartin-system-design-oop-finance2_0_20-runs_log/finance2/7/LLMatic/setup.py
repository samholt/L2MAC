from setuptools import setup, find_packages

setup(
    name='FinancialApp',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'flask_marshmallow',
        'marshmallow-sqlalchemy',
        'flask_jwt_extended',
        'flask_bcrypt',
        'matplotlib',
        'numpy',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'financialapp = app:main'
        ]
    }
)
