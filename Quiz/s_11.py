# Implemnets decorator to cache func
from functools import lru_cache
import time


def memorize(f):
	cache = {}

	def _wrapper(n):
		if n not in cache:
			cache[n] = f(n)
		return cache[n]
	return _wrapper

@memorize
def long_func(num: int) -> int:
	r = 0
	for i in range(1000000):
		r += num * i
	return r


if __name__ == '__main__':
	for i in range(10):
		print(long_func(3))
	start = time.time()
	for i in range(10):
		print(long_func(i))
	print(time.time() - start)
