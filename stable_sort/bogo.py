# 不安定ソート
# Ave: (n+1)!, Best: n, worst: Unbounded, 安定: NO

import random
from typing import List


def in_order(numbers: list) -> bool:
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))
# all: ()内のすべて判定がTrueになればTrueを返す


def bogo_sort(numbers) -> List[int]:
    while not in_order(numbers):
        random.shuffle(numbers)
    return numbers


if __name__ == '__main__':
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(bogo_sort(nums))
