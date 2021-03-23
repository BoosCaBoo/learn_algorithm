"""
Input x: [1, 2, 3 ,4, 4, 5, 5, 8, 10] y: [4, 5, 5, 5, 6, 7, 8, 8, 10]
   -> x: [1, 2, 3, 4, 4, 10]          y: [5, 5, 5, 6, 7, 8, 8, 10]
"""

from typing import List


def min_count_remove(x: List[int], y : List[int]) -> None:
	count_x = {}
	count_y = {}
