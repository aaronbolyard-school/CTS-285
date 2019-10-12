from memory_bank import MemoryBank
from operation import Add
from problem import Problem

def test_should_store_problem_in_memory_bank():
	memory_bank = MemoryBank()
	problem = Problem(Add())

	result = memory_bank.add(problem)

	assert(len(memory_bank) == 1)
	assert(memory_bank[0] == problem)
	assert(result == True)

def test_should_store_multiple_problems_in_memory_bank():
	memory_bank = MemoryBank()
	problem1 = Problem(Add(), 1, 1)
	problem2 = Problem(Add(), 2, 2)

	result1 = memory_bank.add(problem1)
	result2 = memory_bank.add(problem2)

	assert(len(memory_bank) == 2)
	assert(memory_bank[0] == problem1)
	assert(memory_bank[1] == problem2)
	assert(result1 == True)
	assert(result2 == True)

def test_should_not_store_dupe_problems_in_memory_bank():
	memory_bank = MemoryBank()
	problem1 = Problem(Add())
	problem2 = Problem(Add())

	memory_bank.add(problem1)
	result = memory_bank.add(problem2)

	assert(len(memory_bank) == 1)
	assert(memory_bank[0].isSame(problem1))
	assert(memory_bank[0].isSame(problem2))
	assert(result == False)

def test_should_remove_problem_in_memory_bank():
	memory_bank = MemoryBank()
	problem1 = Problem(Add())
	problem2 = Problem(Add())

	memory_bank.add(problem1)
	result = memory_bank.remove(problem2)

	assert(len(memory_bank) == 0)
	assert(result == True)

def test_should_remove_problem_at_index_in_memory_bank():
	memory_bank = MemoryBank()
	problem = Problem(Add())

	memory_bank.add(problem)
	memory_bank.removeAt(0)

	assert(len(memory_bank) == 0)
