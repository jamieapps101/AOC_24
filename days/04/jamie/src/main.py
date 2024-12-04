import sys
from typing import List
import itertools


def search_at_position(
    grid: List[List[str]], x: int, y: int, x_max: int, y_max: int
) -> int:
    """Looking for XMAS string"""
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


def search_at_position2(
    grid: List[List[str]], x: int, y: int, x_max: int, y_max: int
) -> bool:
    """Looking for X shaped MAS string"""
    # check bounds
    if x == 0 or x == x_max - 1 or y == 0 or y == y_max - 1:
        return False

    # check center element
    if grid[x][y] != "a":
        return False

    count = sum(
        itertools.starmap(
            lambda i, j: grid[x - i][y - j] == "m" and grid[x + i][y + j] == "s",
            itertools.product([-1, 1], repeat=2),
        )
    )

    # we expect matches on 2 diagonals
    return count == 2


def main():
    s = sys.stdin.read()
    grid = [[c.lower() for c in l] for l in s.splitlines()]
    y_max = len(grid)
    x_max = 0 if y_max == 0 else len(grid[0])
    count = sum(
        itertools.starmap(
            lambda x, y: search_at_position2(grid, x, y, x_max, y_max),
            itertools.product(range(x_max), range(y_max)),
        )
    )
    print(f"{count=}")


if __name__ == "__main__":
    main()


def test_part_2():
    data = [
        ".M.S......",
        "..A..MSMS.",
        ".M.S.MAA..",
        "..A.ASMSM.",
        ".M.S.M....",
        "..........",
        "S.S.S.S.S.",
        ".A.A.A.A..",
        "M.M.M.M.M.",
        "..........",
    ]
    grid = [[c.lower() for c in l] for l in data]
    y_max = len(grid)
    x_max = 0 if y_max == 0 else len(grid[0])
    count = sum(
        itertools.starmap(
            lambda x, y: search_at_position2(grid, x, y, x_max, y_max),
            itertools.product(range(x_max), range(y_max)),
        )
    )
    assert count == 9
