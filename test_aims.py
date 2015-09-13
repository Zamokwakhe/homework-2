from nose.tools import assert_equal
import aims

def test_ints():
	numbers = [2,2]
	obs = aims.std(numbers)
	exp =  0
	assert_equal(obs,exp)


def test_ints():
	numbers = [4,2 ,5 ,8,6]
	obs = aims.std(numbers)
	exp =  2.2360679774997898 
	assert_equal(obs,exp)
