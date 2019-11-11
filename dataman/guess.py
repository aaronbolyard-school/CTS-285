from input import get_integer_from_user, get_should_continue
from random import uniform

def guesser(number):
	attempts = 0
	while True:
		guess = get_integer_from_user('What is your guess? ')
		if guess < number:
			print('The number is higher.')
		elif guess > number:
			print('The number is lower.')
		else:
			print('You guessed right!')
			print('You got the answer in', attempts, 'attempt(s)!')
			return

		attempts = attempts + 1

def main(app):
	while True:
		guesser(round(uniform(1, 100)))

		if not get_should_continue('Do you want to continue? [Y]es/[N]o: '):
			break

if __name__ == '__main__':
	main()
