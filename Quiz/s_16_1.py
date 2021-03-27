from typing import List, Generator


def generate_promes_v1(number: int) -> List:
	primes = []
	i = 0
	for x in range(2, number + 1):
		for y in range(2, x):
			if x % y == 0:
				break
			i += 1
		else:
			primes.append(x)
			i += 1
	print("v1=", i)
	return primes


def generate_promes_v2(number: int) -> List:
	primes = []
	cache = {}
	i = 1
	for x in range(2, number + 1):
		is_prime = cache.get(x)
		if is_prime is False:
			continue
		primes.append(x)
		cache[x] = True
		i += 1
		for y in range(x*2, number+1, x):
			cache[y] = False
			i += 1
	print("v2=", i)
	return primes


def generate_promes_v3(number: int) -> Generator[int, None, None]:
	cache = {}
	for x in range(2, number + 1):
		is_prime = cache.get(x)
		if is_prime is False:
			continue
		yield x
		cache[x] = True
		for y in range(x*2, number+1, x):
			cache[y] = False


if __name__ == '__main__':
	import time
	start1 = time.time()
	print(generate_promes_v1(50))
	print(time.time() - start1)

	start2 = time.time()
	print(generate_promes_v2(50))
	print(time.time() - start2)

	start3 = time.time()
	print([i for i in generate_promes_v3(50)])
	print(time.time() - start3)
