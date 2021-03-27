from typing import List, Tuple
from collections import defaultdict


def taix_cab_number(max_answer_num: int, match_answer_num: int = 2, start_answer: int = 1) -> List[Tuple[int, List[Tuple[int, int]]]]:
	result = []
	got_answer_count = 0
	answer = start_answer
	while got_answer_count < max_answer_num:
		match_answer_count = 0
		memo = defaultdict(list)

		max_param = int(pow(answer, 1.0 / 3)) + 1
		for x in range(1, max_param):
			for y in range(x+1, max_param):
				if x ** 3 + y ** 3 == answer:
					match_answer_count += 1
					memo[answer].append((x, y))

		if match_answer_count == match_answer_num:
			result.append((answer, memo[answer]))
			got_answer_count += 1

		answer += 1

	return result


if __name__ == '__main__':
	import time
	start = time.time()

	print(taix_cab_number(1, 2))
	print(time.time() - start)

	print(taix_cab_number(1, 3, 87539319))
	print(time.time() - start)