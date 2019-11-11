from memory_bank import MemoryBank, memory
from checker import checker
from guess import main as guesser
from input import get_integer_from_user

class App:
	def __init__(self):
		self.memoryBank = MemoryBank()

OPTIONS = {
	1: checker,
	2: memory,
	3: guesser
}

def main():
	app = App()
	print('Welcome to DATAMAN!')

	while True:
		print()
		print('Select an option to continue.')
		print()
		print('0. Quit')
		print('1. Answer Checker')
		print('2. Memory Bank')
		print('3. Number Guesser')

		option = get_integer_from_user('> ')
		operation = OPTIONS.get(option, None)

		if operation:
			operation(app)
		elif option == 0:
			break
		else:
			print('Please select a valid option.')

	print()
	print('Good-bye!')

if __name__ == '__main__':
	main()
