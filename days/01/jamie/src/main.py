import sys
from typing import List, Tuple


def load_data() -> Tuple[List[int], List[int]]:
    list_l = []
    list_r = []
    for line in sys.stdin.readlines():
        components = line.split()
        list_l.append(int(components[0]))
        list_r.append(int(components[1]))
    return (list_l, list_r)


def main():
    list_l, list_r = load_data()
    score = sum(v * sum(v == q for q in list_r) for v in list_l)
    print(f"score: {score}")


if __name__ == "__main__":
    main()
