class Operation:
	def perform(self, left, right):
		pass

	def display(self, left, right):
		pass

class Add(Operation):
	def perform(self, left, right):
		return left + right

	def display(self, left, right):
		return str.format('{} + {}', left, right)

class Sub(Operation):
	def perform(self, left, right):
		return left - right

	def display(self, left, right):
		return str.format('{} - {}', left, right)

class Divide(Operation):
	def perform(self, left, right):
		return left / right

	def display(self, left, right):
		return str.format('{} / {}', left, right)

class Multiply(Operation):
	def perform(self, left, right):
		return left * right

	def display(self, left, right):
		return str.format('{} * {}', left, right)
