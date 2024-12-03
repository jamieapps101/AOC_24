import re
import sys


def main():
    s = sys.stdin.read()
    sum = 0
    for match in re.finditer(r"mul\(([0-9]+),([0-9]+)\)", s):
        sum += int(match.group(1)) * int(match.group(2))
    print(f"{sum=}")


if __name__ == "__main__":
    main()
