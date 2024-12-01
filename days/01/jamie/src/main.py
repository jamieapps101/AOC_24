import sys
from typing import List, Tuple


def load_data() -> Tuple[List[int], List[int]]:
    list_a = []
    list_b = []
    for line in sys.stdin.readlines():
        components = line.split()
        list_a.append(int(components[0]))
        list_b.append(int(components[1]))
    return (list_a, list_b)


def main():
    list_a, list_b = load_data()
    list_a.sort()
    list_b.sort()
    diff = sum(abs(a - b) for a, b in zip(list_a, list_b))
    print(f"dif: {diff}")


if __name__ == "__main__":
    main()
