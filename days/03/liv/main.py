from typing import List
import re

FILE_PATH = "days/03/liv/data/input_data.txt"

def read_file(file_path: str) -> str:
    input_data = ""
    with open(file_path) as fp:
        for char in fp:
            input_data = input_data + char
        # print(input_data)
    return input_data

def strip_disabled_muls(full_list: str) -> str:
    toggle = "do()"
    parsed_string = ""
    for letter in full_list:
        # print("Current letter: ",letter)
        # print("Current parsed string: ",parsed_string)
        if toggle == "do()" and parsed_string[-7:] != "don't()":
            parsed_string = parsed_string + letter
            # print("Toggle is do and no disable statement found - letter added to parsed string: ",parsed_string)
        elif toggle == "do()" and parsed_string[-7:] == "don't()":
            toggle = "don't()"
            # print("Disable statement found! Toggle disabled")
            if re.match(r'(m|u|l)',letter) is not None:
                print("MUL value found - do not append!")
            else:
                parsed_string = parsed_string + letter
                # print("Toggle changed to don't - non-MUL letter added to parsed string: ",parsed_string)
        elif toggle == "don't()" and parsed_string[-4:] != "do()":
            if re.match(r'(m|u|l)',letter) is not None:
                print("MUL value found - do not append!")
            else:
                parsed_string = parsed_string + letter
                # print("Toggle is don't and no enable statement found - non-MUL letter added to parsed string: ",parsed_string)
        elif toggle == "don't()" and parsed_string[-4:] == "do()":
            toggle = "do()"
            # print("Enable statement found! Toggle enabled")
            parsed_string = parsed_string + letter
            # print("Toggle changed to do - letter added to parsed string: ",parsed_string)
        else:
            print("Error!")
    # print("Final parsed string: ",parsed_string)
    return parsed_string

        # Make sure toggle is set correctly - look at end of parsed string and set toggle appropriately.
        # If toggle = do, append to parsed string
        # If toggle = don't, do not append m,u,l to the parsed string

def find_multiplication(memory: str) -> int:
    valid_muls = re.findall(r'mul\([0-9]+,[0-9]+\)',memory)
    # print("Valid: ",valid_muls)
    return valid_muls

def multiply(values: List[str]) -> int:
    multiplication_total = 0
    for sum in values:
        # print("Sum: ",sum)
        numbers = re.search(r'([0-9]+).*?([0-9]+)',sum)
        # print("Values after regex: ",numbers.group)
        first_value = int(numbers.group(1))
        # print("First value: ",first_value)
        second_value = int(numbers.group(2))
        # print("Second value: ",second_value)
        result = first_value * second_value
        multiplication_total = multiplication_total + result
    print("Current multiplication total = ",multiplication_total)

def main():
    input_data = read_file(FILE_PATH)
    parsed_input = strip_disabled_muls(input_data)
    # print("Parsed input from main: ",parsed_input)
    valid_sums = find_multiplication(parsed_input)
    multiply(valid_sums)

if __name__ == "__main__":
    main()