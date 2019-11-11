from input import get_integer_from_user, get_should_continue
from operation import Add, Sub, Multiply, Divide
from problem import Problem

OPERATIONS = {
	1: Add,
	2: Sub,
	3: Multiply,
	4: Divide
}

def get_operand():
	while True:
		result = get_integer_from_user('Please enter a number from 0-100: ')

		if result >= 1 and result <= 100:
			return result
		else:
			print('Number outside of range.')


def program(app):
	while True:
		print()
		print('Please select an operation.')
		print()
		print('1. Add')
		print('2. Subtract')
		print('3. Multiply')
		print('4. Divide')

		option = get_integer_from_user('> ')
		operation = OPERATIONS.get(option, None)

		if operation:
			left = get_operand()
			right = get_operand()

			problem = Problem(operation(), left, right)

			result = str.format('{} = ?', problem.displayWithoutAnswer())
			print('Problem:', result)

			if app:
				app.memoryBank.add(problem)
		else:
			print('Please select a valid option.')

		if not get_should_continue('Do you wish to continue? [Y]es/[N]o: '):
			break

if __name__ == '__main__':
	program(None)
