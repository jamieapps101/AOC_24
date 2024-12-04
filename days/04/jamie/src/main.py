import sys
from typing import List
import itertools


def search_at_position(
    grid: List[List[str]], x: int, y: int, x_max: int, y_max: int
) -> int:
    count = 0
    ref = ["x", "m", "a", "s"]
    for x_delta in [-1, 0, 1]:
        for y_delta in [-1, 0, 1]:
            # skip pointless case
            if x_delta == 0 and y_delta == 0:
                continue
            # check bounds
            in_bounds = (
                x + 3 * x_delta < x_max
                and x + 3 * x_delta >= 0
                and y + 3 * y_delta < y_max
                and y + 3 * y_delta >= 0
            )
            if not in_bounds:
                continue

            # evaluate
            found = True
            for i in range(4):
                if grid[x + x_delta * i][y + y_delta * i] != ref[i]:
                    found = False
                    break

            if found:
                count += 1

    return count


def main():
    s = sys.stdin.read()
    grid = [[c.lower() for c in l] for l in s.splitlines()]
    y_max = len(grid)
    x_max = 0 if y_max == 0 else len(grid[0])
    count = sum(
        itertools.starmap(
            lambda x, y: search_at_position(grid, x, y, x_max, y_max),
            itertools.product(range(x_max), range(y_max)),
        )
    )
    print(f"{x_max=}")
    print(f"{y_max=}")
    print(f"{count=}")


if __name__ == "__main__":
    main()
