from typing import List, Tuple
import itertools
import sys


def is_not_solvable(answer: int, values: List[int]) -> bool:
    # print(f"{answer}: {values} ",end="")
    operator_iter = itertools.product([0, 1], repeat=len(values) - 1)
    eval_iter = map(lambda operators: evaluate(values, operators), operator_iter)
    correct = itertools.filterfalse(lambda v: v != answer, eval_iter)
    try:
        _ = next(correct)
        # print("is solveable")
        return False
    except StopIteration:
        # print("is not solveable")
        return True


def evaluate(values: List[int], operators: List[int]) -> int:
    out = values[0]
    for val, op in zip(values[1:], operators):
        match op:
            case 0:
                out *= val
            case 1:
                out += val
            case _:
                raise ValueError
    return out


def process_line(line: str) -> Tuple[int, List[int]]:
    components = line.split(":")
    answer = int(components[0])
    values = [int(v) for v in components[1].split()]
    return (answer, values)


def main():
    data = map(process_line, sys.stdin)
    solveable_eqns = itertools.filterfalse(
        lambda args: is_not_solvable(args[0], args[1]), data
    )
    answers = itertools.starmap(lambda answer, _values: answer, solveable_eqns)
    # answers = list(answers)
    # print(f"{answers=}")
    total = sum(answers)
    print(f"{total=}")


if __name__ == "__main__":
    main()


def test_is_solvable():
    assert not is_not_solvable(190, [10, 19])
    assert not is_not_solvable(3267, [81, 40, 27])
    assert is_not_solvable(83, [17, 5])
    assert is_not_solvable(156, [15, 6])
    assert is_not_solvable(7290, [6, 8, 6, 15])
    assert is_not_solvable(161011, [16, 10, 13])
    assert is_not_solvable(192, [17, 8, 14])
    assert is_not_solvable(21037, [9, 7, 18, 13])
    assert not is_not_solvable(292, [11, 6, 16, 20])
