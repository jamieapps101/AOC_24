from typing import List
import re

FILE_PATH = "days/03/liv/data/input_data.txt"

def read_file(file_path: str) -> str:
    input_data = ""
    with open(file_path) as fp:
        for char in fp:
            input_data = input_data + char
        print(input_data)
    return input_data

def find_multiplication(memory: str) -> int:
    valid_muls = re.findall(r'mul\([0-9]+,[0-9]+\)',memory)
    print("Valid: ",valid_muls)
    return valid_muls

def multiply(values: List[str]) -> int:
    multiplication_total = 0
    for sum in values:
        print("Sum: ",sum)
        numbers = re.search(r'([0-9]+).*?([0-9]+)',sum)
        # print("Values after regex: ",numbers.group)
        first_value = int(numbers.group(1))
        print("First value: ",first_value)
        second_value = int(numbers.group(2))
        print("Second value: ",second_value)
        result = first_value * second_value
        multiplication_total = multiplication_total + result
        print("Current multiplication total = ",multiplication_total)

def main():
    input_data = read_file(FILE_PATH)
    valid_sums = find_multiplication(input_data)
    multiply(valid_sums)

if __name__ == "__main__":
    main()