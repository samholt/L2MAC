from setuptools import setup, find_packages

setup(
    name='twitter_clone',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Add any additional packages you've used here
    ],
    entry_points='''
        [console_scripts]
        twitter_clone=main:main
    ''',
)
