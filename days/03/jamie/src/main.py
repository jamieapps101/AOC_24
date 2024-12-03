import re
import sys


def main():
    s = sys.stdin.read()
    sum = 0
    enabled = True
    for match in re.finditer(r"mul\(([0-9]+),([0-9]+)\)|do\(\)|don't\(\)", s):
        if match.group(0) == "do()":
            enabled = True
        elif match.group(0) == "don't()":
            enabled = False
        elif enabled:
            sum += int(match.group(1)) * int(match.group(2))
    print(f"{sum=}")


if __name__ == "__main__":
    main()
