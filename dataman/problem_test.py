from operation import Add
from problem import Problem

def test_solve_to_correct_answer():
	problem = Problem(Add(), 2, 2)

	assert(problem.solve() == 4)

def test_clamp_inputs_to_1_if_below_0():
	problem = Problem(Add(), -1, -1)

	assert(problem.displayWithoutAnswer() == '1 + 1')

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
