class Problem:
	def __init__(self, operation, lhs=1, rhs=1):
		self._operation = operation
		self._left = round(max(lhs, 1))
		self._right = round(max(rhs, 1))

	def isSame(self, other):
		if not isinstance(other._operation, type(self._operation)):
			return False

		if self._left != other._left or self._right != other._right:
			return False

		return True

	def solve(self):
		return self._operation.perform(self._left, self._right)

	def isCorrect(self, answer):
		return self.solve() == answer

	def displayWithoutAnswer(self):
		return self._operation.display(self._left, self._right)

	def displayWithAnswer(self):
		lhs = self.displayWithoutAnswer()
		rhs = self.solve()

		return str.format('{} = {}', lhs, rhs)
