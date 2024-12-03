from typing import List
import re

FILE_PATH = "days/02/liv/data/input_data.txt"

def read_file(file_path: str) -> List[List[int]]:
    reports = []
    with open(file_path) as fp:
        for line in fp:
            line = line.split()
            print("Line: ",line)
            int_lines = []
            for number in line:
                number = int(number)
                int_lines.append(number)
            print("Int_Lines: ",int_lines)
            reports.append(int_lines)
            # report_line = ""
            # for char in line:
            #     if re.match(r"[0-9]",char) is None:
            #         continue
            #     elif re.match(r"[0-9]",char) is not None:
            #         report_line = report_line + char
            #     else:
            #         print("Error")
            # # report_line = int(report_line)
            # reports.append(report_line)
    print("Report: ",reports)
    return reports

def check_report(report: List[int]) -> int:
    increase_count = 0
    decrease_count = 0
    difference = 0
    safe_number = 0
    for level_count in range(len(report)):
        print("Level Count: ",level_count)
        print("Report: ",report)
        print("Line Length: ",len(report))
        print("Level Value: ",report[level_count])
        print("Level Count + 1: ",level_count + 1)
        if level_count == len(report) - 1:
            print("End of line")
            continue
        elif report[level_count] == report[level_count + 1]:
            print("Level values are identical - unsafe report")
            break
        elif report[level_count] < report[level_count + 1]:
            difference = report[level_count + 1] - report[level_count]
            print("Difference: ",difference)
            if difference > 3:
                print("Difference greater than 3 - unsafe report")
                break
            else:
                increase_count = increase_count + 1
                print("Increase counter incremented: ",increase_count)
        elif report[level_count] > report[level_count + 1]:
            difference = report[level_count] - report[level_count + 1]
            print("Difference: ",difference)
            if difference > 3:
                print("Difference greater than 3 - unsafe report")
                break
            else:
                decrease_count = decrease_count + 1
                print("Decrease counter incremented: ",decrease_count)
        else:
            print("Error - missing scenario")
        print("Increase count at end of report: ",increase_count)
        print("Decrease count at end of report: ",decrease_count)
        if increase_count == len(report) - 1 and decrease_count == 0:
            print("Only increasing - safe report!")
            safe_number = safe_number + 1
            # print("Safe number of reports: ",safe_number)
        elif decrease_count == len(report) - 1 and increase_count == 0:
            print("Only decreasing - safe report!")
            safe_number = safe_number + 1
            # print("Safe number of reports: ",safe_number)
        else:
            print("Unsafe report")
    if safe_number == 1:
        print("Report is safe")
    else:
        print("Report is unsafe")
    return safe_number

def safety_checker(reports: List[List[int]]) -> int:
    safe_number = 0
    for report in reports:
        if check_report(report) == 1:
            safe_number = safe_number + 1
        else:
            for number in range(len(report)):
                report_copy = report.copy()
                report_copy.pop(number)
                print("Report after number removed: ",report_copy)
                if check_report(report_copy) == 1:
                    print("Report is safe!")
                    safe_number = safe_number + 1
                    break
                else:
                    print("Report unsafe!")
    print("Final safe number of reports: ",safe_number)
    return safe_number

def main():
    input_data = read_file(FILE_PATH)
    # print("From main: ",input_data)
    safe_reports = safety_checker(input_data)

if __name__ == "__main__":
    main()

# Go one layer out - don't look at chars, look at whole values and see if you can index into the next value in the list. Use index but derive it somehow? Use range one layer back in the for loop?
# Len won' work to derive increase and decrease - change to count items in the list?