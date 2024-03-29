from operation import Add
from problem import Problem

def test_solve_to_correct_answer():
	problem = Problem(Add(), 2, 2)

	assert(problem.solve() == 4)

def test_clamp_inputs_to_1_if_below_0():
	problem = Problem(Add(), -1, -1)

	assert(problem.displayWithoutAnswer() == '1 + 1')

def test_round_inputs():
	problem = Problem(Add(), 0.1, 3.6)

	assert(problem.displayWithoutAnswer() == '1 + 4')

def test_return_false_if_answer_is_wrong():
	problem = Problem(Add(), 2, 2)

	assert(problem.isCorrect(5) == False)

def test_return_true_if_answer_is_correct():
	problem = Problem(Add(), 2, 2)

	assert(problem.isCorrect(4) == True)

def test_display_without_answer_correctly():
	problem = Problem(Add(), 2, 2)

	assert(problem.displayWithoutAnswer() == '2 + 2')	

def test_display_with_answer_correctly():
	problem = Problem(Add(), 2, 2)

	assert(problem.displayWithAnswer() == '2 + 2 = 4')	

def test_isSame_should_return_true_if_both_operations_are_same():
	problem1 = Problem(Add(), 2, 2)
	problem2 = Problem(Add(), 2, 2)

	assert(problem1.isSame(problem2))

def test_isSame_should_return_false_if_both_operations_are_not_same():
	problem1 = Problem(Add(), 2, 2)
	problem2 = Problem(Add(), 4, 0)

	assert(not problem1.isSame(problem2))
