import re
import sys


def main():
    s = sys.stdin.read()
    sum = 0
    enabled = True
    for match in re.finditer(r"mul\(([0-9]+),([0-9]+)\)|do\(\)|don't\(\)", s):
        if len(match.group(0)) == 4:
            enabled = True
        elif len(match.group(0)) == 7:
            enabled = False
        else:
            sum += enabled*int(match.group(1)) * int(match.group(2))
    print(f"sum: {sum}")


if __name__ == "__main__":
    main()
