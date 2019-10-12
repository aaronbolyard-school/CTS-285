def get_integer_from_user(prompt):
	while True:
		print(prompt, end='')
		result = input()

		try:
			return int(result)
		except:
			print('Please enter an integer.')

def get_should_continue(prompt='Do you want to continue? [Y]es/[N]o: '):
	while True:
		print(prompt, end='')

		result = input().lower()
		if result == 'y':
			return True
		elif result == 'n':
			return False
		else:
			print('Please enter "y" for yes or "n" for no.')
