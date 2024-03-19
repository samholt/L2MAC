from setuptools import setup, find_packages

setup(
	name='task_60',
	version='1.0.0',
	packages=find_packages(),
	author='ChatGPT',
	author_email='chatgpt@openai.com',
	description='A package to sum numbers from 1 to n',
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	url='https://github.com/openai/task_60',
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
	],
	python_requires='>=3.6',
)
