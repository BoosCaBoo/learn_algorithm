from typing import List

def get_max_sequence_sum(numbers: List[int]) ->int:
	result_sequence, sum_sequence = 0, 0
	for num in numbers:
		temp = 1
