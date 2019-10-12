from input import get_integer_from_user, get_should_continue

class MemoryBank:
	def __init__(self):
		self.problems = []

	def add(self, problem):
		for p in self:
			if p.isSame(problem):
				return False

		self.problems.append(problem)
		return True

	def remove(self, problem):
		index = 0
		for p in self:
			if p.isSame(problem):
				self.problems.pop(index)
				return True
			else:
				index += 1
		return False

	def removeAt(self, index):
		self.problems.pop(index)

	def __len__(self):
		return len(self.problems)

	def __iter__(self):
		return iter(self.problems)

	def __getitem__(self, index):
		return self.problems[index]

def memory(app):
	if not app or len(app.memoryBank) == 0:
		print('No problems in memory bank. Sorry!')
		return

	print(str.format('Welcome to Memory Bank! There are {} problems.', len(app.memoryBank)))

	index = 0
	while index < len(app.memoryBank):
		problem = app.memoryBank[0]

		print()
		prompt = str.format('{} = ', problem.displayWithoutAnswer())
		result = get_integer_from_user(prompt)

		if problem.isCorrect(result):
			print('Correct!')

			message = 'Do you want to remove this from the Memory Bank? [Y]es/[N]o: '
			if get_should_continue(message):
				app.memoryBank.removeAt(index)
				continue
		else:
			print('Incorrect!')
			print(problem.displayWithAnswer())

		index += 1

	print()
	print('That was the last problem!')
