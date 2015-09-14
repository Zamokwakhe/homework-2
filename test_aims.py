from nose.tools import assert_equal
import aims

def test_ints():
	numbers = [2,2]
	obs = aims.std(numbers)
	exp =  0
	assert_equal(obs,exp)


def test_ints1():
	numbers = [4,2 ,5 ,8,6]
	obs = aims.std(numbers)
	exp =  2.2360679774997898 
	assert_equal(obs,exp)

def test_ints2():
	obs = aims.avg_range(['data/bert/audioresult-00215'])
	exp1 =  5
	assert_equal(obs,exp1)



def test_ints3():
	obs = aims.avg_range(['data/bert/audioresult-00223'])
	exp1 =  2
	assert_equal(obs,exp1)


def test_ints4():
	obs = aims.avg_range(['data/bert/audioresult-00246'])
	exp1 =  8
	assert_equal(obs,exp1)

