from typing import List

FILE_PATH = "days/04/liv/data/input_data.txt"

def read_file(file_path: str) -> List[str]:
    lines = []
    with open(file_path) as fp:
        for line in fp:
            line = line.rstrip()
            lines.append(line)
    print(lines)
    return lines

def down_check(input_data: List[str], line_index: int, char_index: int, line_length: int) -> bool:
    if line_index + 3 <= line_length and input_data[line_index + 1][char_index] == "M" and input_data[line_index + 2][char_index] == "A" and input_data[line_index + 3][char_index] == "S":
        check_result = True
    else:
        check_result = False
    return check_result

def up_check(input_data: List[str], line_index: int, char_index: int, line_length: int) -> bool:
    if line_index - 3 >=0 and input_data[line_index - 1][char_index] == "M" and input_data[line_index - 2][char_index] == "A" and input_data[line_index - 3][char_index] == "S":
        check_result = True
    else:
        check_result = False
    return check_result

def left_check(input_data: List[str], line_index: int, char_index: int, line_length: int) -> bool:
    if char_index - 3 >=0 and input_data[line_index][char_index - 1] == "M" and input_data[line_index][char_index - 2] == "A" and input_data[line_index][char_index - 3] == "S":
        check_result = True
    else:
        check_result = False
    return check_result

def right_check(input_data: List[str], line_index: int, char_index: int, line_length: int) -> bool:
    # print("Right + 1: ",input_data[line_index][char_index + 1])
    # print("Right + 2: ",input_data[line_index][char_index + 2])
    # print("Right + 3: ",input_data[line_index][char_index + 3])
    if char_index + 3 <= line_length and input_data[line_index][char_index + 1] == "M" and input_data[line_index][char_index + 2] == "A" and input_data[line_index][char_index + 3] == "S":
        check_result = True
    else:
        check_result = False
    return check_result

def diagonal_left_up_check(input_data: List[str], line_index: int, char_index: int, line_length: int) -> bool:
    # print("Diagonal Left Up + 1: ",input_data[line_index - 1][char_index - 1])
    # print("Diagonal Left Up + 1 Coords: ",line_index - 1,char_index - 1)
    # print("Diagonal Left Up + 2: ",input_data[line_index - 2][char_index - 2])
    # print("Diagonal Left Up + 2 Coords: ",line_index - 2,char_index - 2)
    # print("Diagonal Left Up + 3: ",input_data[line_index - 3][char_index - 3])
    # print("Diagonal Left Up + 3 Coords: ",line_index - 3,char_index - 3)
    if line_index - 3 >=0 and char_index - 3 >=0 and input_data[line_index - 1][char_index - 1] == "M" and input_data[line_index - 2][char_index - 2] == "A" and input_data[line_index - 3][char_index - 3] == "S":
        check_result = True
    else:
        check_result = False
    return check_result

def diagonal_right_up_check(input_data: List[str], line_index: int, char_index: int, line_length: int) -> bool:
    if char_index + 3 <= line_length and line_index - 3 >=0 and input_data[line_index - 1][char_index + 1] == "M" and input_data[line_index - 2][char_index + 2] == "A" and input_data[line_index - 3][char_index + 3] == "S":
        check_result = True
    else:
        check_result = False
    return check_result

def diagonal_left_down_check(input_data: List[str], line_index: int, char_index: int, line_length: int) -> bool:
    if  line_index + 3 <= line_length and char_index - 3 >=0 and input_data[line_index + 1][char_index - 1] == "M" and input_data[line_index + 2][char_index - 2] == "A" and input_data[line_index + 3][char_index - 3] == "S":
        check_result = True
    else:
        check_result = False
    return check_result

def diagonal_right_down_check(input_data: List[str], line_index: int, char_index: int, line_length: int) -> bool:
    if line_index + 3 <= line_length and char_index + 3 <= line_length and input_data[line_index + 1][char_index + 1] == "M" and input_data[line_index + 2][char_index + 2] == "A" and input_data[line_index + 3][char_index + 3] == "S":
        check_result = True
    else:
        check_result = False
    return check_result

def xmas_checker(lines: List[str]) -> int:
    hit_count = 0
    for line_index in range(len(lines)):
        for char_index in range(len(lines)):
            current_position = line_index,char_index
            print("Current position: ",current_position)
            current_letter = lines[line_index][char_index]
            print("Current letter: ",lines[line_index][char_index])
            print("Line length: ",len(lines))
            if current_letter != "X":
                pass
            elif current_letter == "X":
                if line_index == 0 and char_index == 0:
                    # You are at the top left corner: look down, diagonal down right and right
                    down_check_result = False
                    down_check_result = down_check(lines,line_index,char_index,len(lines) - 1)
                    if down_check_result == True:
                        print("Down check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Down check complete - move to next check!")
                    diagonal_right_down_check_result = False
                    diagonal_right_down_check_result = diagonal_right_down_check(lines,line_index,char_index,len(lines) - 1)
                    if diagonal_right_down_check_result == True:
                        print("Diagonal right down check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Diagonal right down check complete - move to next check!")
                    right_check_result = False
                    right_check_result = right_check(lines,line_index,char_index,len(lines) - 1)
                    if right_check_result == True:
                        print("Right check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Right check complete - final check completed")
                elif line_index == 0 and char_index == len(lines) - 1:
                    # You are at the top right corner: look down, diagonal down left and left
                    down_check_result = False
                    down_check_result = down_check(lines,line_index,char_index,len(lines) - 1)
                    if down_check_result == True:
                        print("Down check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Down check complete - move to next check!")
                    diagonal_left_down_check_result = False
                    diagonal_left_down_check_result = diagonal_left_down_check(lines,line_index,char_index,len(lines) - 1)
                    if diagonal_left_down_check_result == True:
                        print("Diagonal left down check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Diagonal left down check complete - move to next check!")
                    left_check_result = False
                    left_check_result = left_check(lines,line_index,char_index,len(lines) - 1)
                    if left_check_result == True:
                        print("Left check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Left check complete - final check completed")
                elif line_index == len(lines) - 1 and char_index == 0:
                    # You are at the bottom left corner: look up, diagonal up right and right
                    up_check_result = False
                    up_check_result = up_check(lines,line_index,char_index,len(lines) - 1)
                    if up_check_result == True:
                        print("Up check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Up check complete - move to next check!")
                    diagonal_right_up_check_result = False
                    diagonal_right_up_check_result = diagonal_right_up_check(lines,line_index,char_index,len(lines) - 1)
                    if diagonal_right_up_check_result == True:
                        print("Diagonal right up check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Diagonal right up check complete - move to next check!")
                    right_check_result = False
                    right_check_result = right_check(lines,line_index,char_index,len(lines) - 1)
                    if right_check_result == True:
                        print("Right check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Right check complete - final check completed")
                elif line_index == len(lines) - 1 and char_index == len(lines) - 1:
                    # You are at the bottom right corner: look up, diagonal up left and left
                    up_check_result = False
                    up_check_result = up_check(lines,line_index,char_index,len(lines) - 1)
                    if up_check_result == True:
                        print("Up check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Up check complete - move to next check!")
                    diagonal_left_up_check_result = False
                    diagonal_left_up_check_result = diagonal_left_up_check(lines,line_index,char_index,len(lines) - 1)
                    if diagonal_left_up_check_result == True:
                        print("Diagonal left up check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Diagonal left up check complete - move to next check!")
                    left_check_result = False
                    left_check_result = left_check(lines,line_index,char_index,len(lines) - 1)
                    if left_check_result == True:
                        print("Left check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Left check complete - final check completed")
                elif line_index == 0:
                    # You are on the top line: look down, diagonal down right, diagonal down left, left and right
                    down_check_result = False
                    down_check_result = down_check(lines,line_index,char_index,len(lines) - 1)
                    if down_check_result == True:
                        print("Down check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Down check complete - move to next check!")
                    diagonal_right_down_check_result = False
                    diagonal_right_down_check_result = diagonal_right_down_check(lines,line_index,char_index,len(lines) - 1)
                    if diagonal_right_down_check_result == True:
                        print("Diagonal right down check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Diagonal right down check complete - move to next check!")
                    diagonal_left_down_check_result = False
                    diagonal_left_down_check_result = diagonal_left_down_check(lines,line_index,char_index,len(lines) - 1)
                    if diagonal_left_down_check_result == True:
                        print("Diagonal left down check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Diagonal left down check complete - move to next check!")
                    left_check_result = False
                    left_check_result = left_check(lines,line_index,char_index,len(lines) - 1)
                    if left_check_result == True:
                        print("Left check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Left check complete - move to next check!")
                    right_check_result = False
                    right_check_result = right_check(lines,line_index,char_index,len(lines) - 1)
                    if right_check_result == True:
                        print("Right check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Right check complete - final check completed")
                elif line_index == len(lines) - 1:
                    # You are on the bottom line: look up, diagonal up right, diagonal up left, left and right
                    up_check_result = False
                    up_check_result = up_check(lines,line_index,char_index,len(lines) - 1)
                    if up_check_result == True:
                        print("Up check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Up check complete - move to next check!")
                    diagonal_right_up_check_result = False
                    diagonal_right_up_check_result = diagonal_right_up_check(lines,line_index,char_index,len(lines) - 1)
                    if diagonal_right_up_check_result == True:
                        print("Diagonal right up check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Diagonal right up check complete - move to next check!")
                    diagonal_left_up_check_result = False
                    diagonal_left_up_check_result = diagonal_left_up_check(lines,line_index,char_index,len(lines) - 1)
                    if diagonal_left_up_check_result == True:
                        print("Diagonal left up check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Diagonal left up check complete - move to next check!")
                    left_check_result = False
                    left_check_result = left_check(lines,line_index,char_index,len(lines) - 1)
                    if left_check_result == True:
                        print("Left check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Left check complete - move to next check!")
                    right_check_result = False
                    right_check_result = right_check(lines,line_index,char_index,len(lines) - 1)
                    if right_check_result == True:
                        print("Right check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Right check complete - final check completed")
                elif char_index == 0:
                    # You are on the leftmost edge - start of a line: look up, right, down, diagonal up right, diagonal down right
                    up_check_result = False
                    up_check_result = up_check(lines,line_index,char_index,len(lines) - 1)
                    if up_check_result == True:
                        print("Up check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Up check complete - move to next check!")
                    right_check_result = False
                    right_check_result = right_check(lines,line_index,char_index,len(lines) - 1)
                    if right_check_result == True:
                        print("Right check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Right check complete - move to next check!")
                    down_check_result = False
                    down_check_result = down_check(lines,line_index,char_index,len(lines) - 1)
                    if down_check_result == True:
                        print("Down check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Down check complete - move to next check!")
                    diagonal_right_up_check_result = False
                    diagonal_right_up_check_result = diagonal_right_up_check(lines,line_index,char_index,len(lines) - 1)
                    if diagonal_right_up_check_result == True:
                        print("Diagonal right up check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Diagonal right up check complete - move to next check!")
                    diagonal_right_down_check_result = False
                    diagonal_right_down_check_result = diagonal_right_down_check(lines,line_index,char_index,len(lines) - 1)
                    if diagonal_right_down_check_result == True:
                        print("Diagonal right down check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Diagonal right down check complete - final check completed")
                elif char_index == len(lines) - 1:
                    # You are the the rightmost edge - end of a line: look up, left, down, diagonal up left, diagonal down left
                    up_check_result = False
                    up_check_result = up_check(lines,line_index,char_index,len(lines) - 1)
                    if up_check_result == True:
                        print("Up check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Up check complete - move to next check!")
                    left_check_result = False
                    left_check_result = left_check(lines,line_index,char_index,len(lines) - 1)
                    if left_check_result == True:
                        print("Left check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Left check complete - move to next check!")
                    down_check_result = False
                    down_check_result = down_check(lines,line_index,char_index,len(lines) - 1)
                    if down_check_result == True:
                        print("Down check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Down check complete - move to next check!")
                    diagonal_left_up_check_result = False
                    diagonal_left_up_check_result = diagonal_left_up_check(lines,line_index,char_index,len(lines) - 1)
                    if diagonal_left_up_check_result == True:
                        print("Diagonal left up check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Diagonal left up check complete - move to next check!")
                    diagonal_left_down_check_result = False
                    diagonal_left_down_check_result = diagonal_left_down_check(lines,line_index,char_index,len(lines) - 1)
                    if diagonal_left_down_check_result == True:
                        print("Diagonal left down check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Diagonal left down check complete - final check completed")
                else:
                    # You are in the middle of the grid - look up, diagonal right up, right, diagonal right down, down, diagonal left down, left, diagonal left up
                    up_check_result = False
                    up_check_result = up_check(lines,line_index,char_index,len(lines) - 1)
                    if up_check_result == True:
                        print("Up check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Up check complete - move to next check!")
                    diagonal_right_up_check_result = False
                    diagonal_right_up_check_result = diagonal_right_up_check(lines,line_index,char_index,len(lines) - 1)
                    if diagonal_right_up_check_result == True:
                        print("Diagonal right up check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Diagonal right up check complete - move to next check!")
                    diagonal_left_up_check_result = False
                    diagonal_left_up_check_result = diagonal_left_up_check(lines,line_index,char_index,len(lines) - 1)
                    if diagonal_left_up_check_result == True:
                        print("Diagonal left up check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Diagonal left up check complete - move to next check!")
                    left_check_result = False
                    left_check_result = left_check(lines,line_index,char_index,len(lines) - 1)
                    if left_check_result == True:
                        print("Left check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Left check complete - move to next check!")
                    right_check_result = False
                    right_check_result = right_check(lines,line_index,char_index,len(lines) - 1)
                    if right_check_result == True:
                        print("Right check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Right check complete - move to next check!")
                    down_check_result = False
                    down_check_result = down_check(lines,line_index,char_index,len(lines) - 1)
                    if down_check_result == True:
                        print("Down check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Down check complete - move to next check!")
                    diagonal_right_down_check_result = False
                    diagonal_right_down_check_result = diagonal_right_down_check(lines,line_index,char_index,len(lines) - 1)
                    if diagonal_right_down_check_result == True:
                        print("Diagonal right down check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Diagonal right down check complete - move to next check!")
                    diagonal_left_down_check_result = False
                    diagonal_left_down_check_result = diagonal_left_down_check(lines,line_index,char_index,len(lines) - 1)
                    if diagonal_left_down_check_result == True:
                        print("Diagonal left down check match found! Increment hit count")
                        hit_count = hit_count + 1
                    else:
                        print("Diagonal left down check complete - final check completed")
    print("Final hit count: ",hit_count)
    return hit_count

def main():
    input_data = read_file(FILE_PATH)
    output = xmas_checker(input_data)

if __name__ == "__main__":
    main()