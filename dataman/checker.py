from input import get_integer_from_user, get_should_continue
from random import uniform
from operation import Add, Sub, Multiply, Divide
from problem import Problem

def generate_problem(rangeMin=1, rangeMax=20):
	problem_type = round(uniform(1, 4))

	if problem_type == 1:
		return Problem(Add(), uniform(rangeMin, rangeMax), uniform(rangeMin, rangeMax))
	elif problem_type == 2:
		a = uniform(rangeMin, rangeMax)
		b = uniform(rangeMin, rangeMax)
		return Problem(Sub(), max(a, b), min(a, b))
	elif problem_type == 3:
		return Problem(Add(), uniform(rangeMin, rangeMax), uniform(rangeMin, rangeMax))
	elif problem_type == 4:
		a = round(uniform(rangeMin, rangeMax))
		b = round(uniform(rangeMin, rangeMax))
		c = a * b
		return Problem(Divide(), c, min(a, b))

def checker(app):
	while True:
		problem = generate_problem()

		prompt = str.format('{} = ', problem.displayWithoutAnswer())
		result = get_integer_from_user(prompt)

		if problem.isCorrect(result):
			print('Correct!')
		else:
			print('Incorrect!')
			print(problem.displayWithAnswer())

			if app:
				message = 'Do you want to add this to the Memory Bank? [Y]es/[N]o: '
				if get_should_continue(message):
					app.memoryBank.add(problem)

		if not get_should_continue():
			break

if __name__ == '__main__':
	checker()
