import sys
from enum import Enum
import itertools
import functools
from typing import List, Tuple

DECREASING = -1
NO_DIRECTION = 0
INCREASING = 1


def is_safe(numbers: List[int]) -> bool:
    # check direction
    all_decreasing = all(a > b for a, b in itertools.pairwise(numbers))
    all_increasing = all(a < b for a, b in itertools.pairwise(numbers))
    if all_increasing == all_decreasing:  # ie xnor
        return False

    # check delta
    correct_delta = all(
        d >= 1 and d <= 3
        for d in map(lambda x: abs(x[0] - x[1]), itertools.pairwise(numbers))
    )
    return correct_delta


def main():
    line_iterable = map(lambda l: [int(v) for v in l.split()], sys.stdin)
    safe_line_count = sum(is_safe(line) for line in line_iterable)
    print(f"safe_line_count: {safe_line_count}")


if __name__ == "__main__":
    main()


def test_is_safe():
    test_data = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    assert is_safe(test_data[0])
