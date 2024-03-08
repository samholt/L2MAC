from config import config

print('Deploying application with the following configuration:')
for key, value in config.items():
	print(f'{key}: {value}')

print('Deployment successful!')
