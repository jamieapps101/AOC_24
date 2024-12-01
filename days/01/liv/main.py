from typing import List
import re

FILE_PATH = "days/01/liv/data/input_data.txt"

def read_file(file_path: str) -> List[int]:
    list_1 = []
    list_2 = []
    with open(file_path) as fp:
        print("About to start line for loop!")
        for line in fp:
            line_1 = ""
            print("Line 1 Start: ",line_1)
            line_2 = ""
            print("Line 2 Start: ",line_2)
            current_line = 0
            for char in line:
                print("Char Loop Running!")
                if re.match(r"[0-9]",char) is None:
                    current_line = 1
                    print("Not a number - current_line set to 1!")
                elif re.match(r"[0-9]",char) is not None and current_line == 0:
                    line_1 = line_1 + char
                    print("Char added to line_1 - line_1 = ",line_1)
                elif re.match(r"[0-9]",char) is not None and current_line == 1:
                    line_2 = line_2 + char
                    print("Char added to line_2 - line_2 = ",line_2)
                else:
                    print("Error")
            print("Char loop Line 1: ",line_1)
            print("Char loop Line 2: ",line_2)
            line_1 = int(line_1)
            line_2 = int(line_2)
            list_1.append(line_1)
            list_2.append(line_2)
            print("Char loop List 1: ",list_1)
            print("Char loop List 2: ",list_2)
    print("Final List 1: ",list_1)
    print("Final List 2: ",list_2)
    list_1.sort()
    print("Final Sorted List 1: ",list_1)
    list_2.sort()
    print("Final Sorted List 2: ",list_2)
    return list_1, list_2

def list_comparison(list_1 = List[int], list_2 = List[int]) -> int:
    if len(list_1) == len(list_2):
        print("List lengths match!")
        difference_sum = 0
        for int in range(len(list_1)):
            difference = 0
            print("List 1: ",list_1[int],"List 2: ",list_2[int])
            if list_1[int] >= list_2[int]:
                difference = list_1[int] - list_2[int]
                print("Difference: ",difference)
                difference_sum = difference_sum + difference
                print("List 1 value bigger - difference added to sum")
            elif list_1[int] < list_2[int]:
                difference = list_2[int] - list_1[int]
                print("Difference: ",difference)
                difference_sum = difference_sum + difference
                print("List 2 value bigger - difference added to sum")
            else:
                print("Error")
        print("Difference sum = ",difference_sum)
    return difference_sum

def main():
    list_1, list_2 = read_file(FILE_PATH)
    print("Main List 1: ",list_1)
    print("Main List 2: ",list_2)
    run_comparison = list_comparison(list_1,list_2)
    print(run_comparison)

if __name__ == "__main__":
    main()
