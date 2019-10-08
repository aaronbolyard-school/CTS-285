from operation import Add, Sub, Divide, Multiply

def test_operation_add_sums_numbers():
	operation = Add()

	assert(operation.perform(1, 1) == 2)
	assert(operation.perform(1, -1) == 0)
	assert(operation.perform(-1, -1) == -2)

def test_operation_add_displays_properly():
	operation = Add()

	assert(operation.display(1, 1) == '1 + 1')
	assert(operation.display(1, -1) == '1 + -1')
	assert(operation.display(-1, -1) == '-1 + -1')

def test_operation_sub_subtracts_numbers():
	operation = Sub()

	assert(operation.perform(1, 1) == 0)
	assert(operation.perform(1, -1) == 2)
	assert(operation.perform(-1, -1) == 0)

def test_operation_sub_displays_properly():
	operation = Sub()

	assert(operation.display(1, 1) == '1 - 1')
	assert(operation.display(1, -1) == '1 - -1')
	assert(operation.display(-1, -1) == '-1 - -1')


def test_operation_divide_divides_numbers():
	operation = Divide()

	assert(operation.perform(4, 2) == 2)
	assert(operation.perform(2, 4) == 0.5)
	assert(operation.perform(-4, 2) == -2)
	assert(operation.perform(-4, -2) == 2)

def test_operation_divide_displays_properly():
	operation = Divide()

	assert(operation.display(4, 2) == '4 / 2')
	assert(operation.display(2, 4) == '2 / 4')
	assert(operation.display(-4, 2) == '-4 / 2')
	assert(operation.display(-4, -2) == '-4 / -2')

def test_operation_multiply_multiplies_numbers():
	operation = Multiply()

	assert(operation.perform(2, 2) == 4)
	assert(operation.perform(-2, 2) == -4)
	assert(operation.perform(-2, -2) == 4)

def test_operation_multiply_displays_properly():
	operation = Multiply()

	assert(operation.display(2, 2) == '2 * 2')
	assert(operation.display(-2, 2) == '-2 * 2')
	assert(operation.display(-2, -2) == '-2 * -2')
