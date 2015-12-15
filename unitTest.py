import unittest

def factorial(n):
	if n < 2:
		return 1
	return factorial(n-1)

class FactorialTest(unittest.TestCase):
	def test_factorial_with_arg_1(self):
		expected = 1
		actual = factorial(1)
		self.assertEqual(expected, actual)

if __name__=="__main__":
	unittest.main()
