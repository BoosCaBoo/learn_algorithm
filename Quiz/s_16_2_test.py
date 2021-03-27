import unittest

from Quiz.s_16_2 import is_prime_v1 as is_prime
list_1 = [2, 3, 5, 7, 11, 13, 17, 19]
list_2 = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]


class PrimeTest(unittest.TestCase):
	def test_is_prime_ok(self):
		for i in list_1:
			self.assertTrue(is_prime(i))

	def test_isprime_no(self):
		for i in list_2:
			self.assertFalse(is_prime(i))

	def test_is_primenegative(self):
		self.assertFalse(is_prime(-1))

	def test_is_prime_raise_typeerror(self):
		with self.assertRaises(TypeError):
			is_prime('string')


if __name__ == '__main__':
	unittest.main()




