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

def s_diagonal_left_up_check(input_data: List[str], line_index: int, char_index: int, line_length: int) -> bool:
    # print("Diagonal Left Up + 1: ",input_data[line_index - 1][char_index - 1])
    # print("Diagonal Left Up + 1 Coords: ",line_index - 1,char_index - 1)
    # print("Diagonal Left Up + 2: ",input_data[line_index - 2][char_index - 2])
    # print("Diagonal Left Up + 2 Coords: ",line_index - 2,char_index - 2)
    # print("Diagonal Left Up + 3: ",input_data[line_index - 3][char_index - 3])
    # print("Diagonal Left Up + 3 Coords: ",line_index - 3,char_index - 3)
    if line_index - 1 >=0 and char_index - 1 >=0 and input_data[line_index - 1][char_index - 1] == "S":
        check_result = True
    else:
        check_result = False
    return check_result

def s_diagonal_right_up_check(input_data: List[str], line_index: int, char_index: int, line_length: int) -> bool:
    if char_index + 1 <= line_length and line_index - 1 >=0 and input_data[line_index - 1][char_index + 1] == "S":
        check_result = True
    else:
        check_result = False
    return check_result

def s_diagonal_left_down_check(input_data: List[str], line_index: int, char_index: int, line_length: int) -> bool:
    if  line_index + 1 <= line_length and char_index - 1 >=0 and input_data[line_index + 1][char_index - 1] == "S":
        check_result = True
    else:
        check_result = False
    return check_result

def s_diagonal_right_down_check(input_data: List[str], line_index: int, char_index: int, line_length: int) -> bool:
    if line_index + 1 <= line_length and char_index + 1 <= line_length and input_data[line_index + 1][char_index + 1] == "S":
        check_result = True
    else:
        check_result = False
    return check_result

def m_diagonal_left_up_check(input_data: List[str], line_index: int, char_index: int, line_length: int) -> bool:
    # print("Diagonal Left Up + 1: ",input_data[line_index - 1][char_index - 1])
    # print("Diagonal Left Up + 1 Coords: ",line_index - 1,char_index - 1)
    # print("Diagonal Left Up + 2: ",input_data[line_index - 2][char_index - 2])
    # print("Diagonal Left Up + 2 Coords: ",line_index - 2,char_index - 2)
    # print("Diagonal Left Up + 3: ",input_data[line_index - 3][char_index - 3])
    # print("Diagonal Left Up + 3 Coords: ",line_index - 3,char_index - 3)
    if line_index - 1 >=0 and char_index - 1 >=0 and input_data[line_index - 1][char_index - 1] == "M":
        check_result = True
    else:
        check_result = False
    return check_result

def m_diagonal_right_up_check(input_data: List[str], line_index: int, char_index: int, line_length: int) -> bool:
    if char_index + 1 <= line_length and line_index - 1 >=0 and input_data[line_index - 1][char_index + 1] == "M":
        check_result = True
    else:
        check_result = False
    return check_result

def m_diagonal_left_down_check(input_data: List[str], line_index: int, char_index: int, line_length: int) -> bool:
    if  line_index + 1 <= line_length and char_index - 1 >=0 and input_data[line_index + 1][char_index - 1] == "M":
        check_result = True
    else:
        check_result = False
    return check_result

def m_diagonal_right_down_check(input_data: List[str], line_index: int, char_index: int, line_length: int) -> bool:
    if line_index + 1 <= line_length and char_index + 1 <= line_length and input_data[line_index + 1][char_index + 1] == "M":
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
            if current_letter != "A":
                pass
            elif current_letter == "A":
                if line_index == 0 and char_index == 0:
                    # You are at the top left corner: no match possible
                    print("Top left corner - no need to search!")
                    continue
                elif line_index == 0 and char_index == len(lines) - 1:
                    # You are at the top right corner: no match possible
                    print("Top right corner - no need to search!")
                    continue
                elif line_index == len(lines) - 1 and char_index == 0:
                    # You are at the bottom left corner: no match possible
                    print("Bottom left corner - no need to search!")
                    continue
                elif line_index == len(lines) - 1 and char_index == len(lines) - 1:
                    # You are at the bottom right corner: no match possible
                    print("Bottom right corner - no need to search!")
                    continue
                elif line_index == 0:
                    # You are on the top line: no match possible
                    print("Top line - no need to search!")
                    continue
                elif line_index == len(lines) - 1:
                    # You are on the bottom line: no match possible
                    print("Bottom line - no need to search!")
                    continue
                elif char_index == 0:
                    # You are on the leftmost edge - no match possible
                    print("Leftmost edge - no need to search!")
                    continue
                elif char_index == len(lines) - 1:
                    # You are the the rightmost edge - no match possible
                    print("Rightmost edge - no need to search!")
                    continue
                else:
                    # You are in the middle of the grid - search all four diagonals; if left up/right down or left down/right up both true, hit.
                    s_diagonal_right_up_check_result = False
                    s_diagonal_right_up_check_result = s_diagonal_right_up_check(lines,line_index,char_index,len(lines) - 1)
                    print("S diagonal right up check result: ",s_diagonal_right_up_check_result)
                    m_diagonal_right_up_check_result = False
                    m_diagonal_right_up_check_result = m_diagonal_right_up_check(lines,line_index,char_index,len(lines) - 1)
                    print("M diagonal right up check result: ",m_diagonal_right_up_check_result)
                    s_diagonal_left_up_check_result = False
                    s_diagonal_left_up_check_result = s_diagonal_left_up_check(lines,line_index,char_index,len(lines) - 1)
                    print("S diagonal left up check result: ",s_diagonal_left_up_check_result)
                    m_diagonal_left_up_check_result = False
                    m_diagonal_left_up_check_result = m_diagonal_left_up_check(lines,line_index,char_index,len(lines) - 1)
                    print("M diagonal left up check result: ",m_diagonal_left_up_check_result)
                    s_diagonal_right_down_check_result = False
                    s_diagonal_right_down_check_result = s_diagonal_right_down_check(lines,line_index,char_index,len(lines) - 1)
                    print("S diagonal right down check result: ",s_diagonal_right_down_check_result)
                    m_diagonal_right_down_check_result = False
                    m_diagonal_right_down_check_result = m_diagonal_right_down_check(lines,line_index,char_index,len(lines) - 1)
                    print("M diagonal right down check result: ",m_diagonal_right_down_check_result)
                    s_diagonal_left_down_check_result = False
                    s_diagonal_left_down_check_result = s_diagonal_left_down_check(lines,line_index,char_index,len(lines) - 1)
                    print("S diagonal left down check result: ",s_diagonal_left_down_check_result)
                    m_diagonal_left_down_check_result = False
                    m_diagonal_left_down_check_result = m_diagonal_left_down_check(lines,line_index,char_index,len(lines) - 1)
                    print("M diagonal left down check result: ",m_diagonal_left_down_check_result)
                    if s_diagonal_right_up_check_result == True and m_diagonal_left_down_check_result == True and s_diagonal_left_up_check_result == True and m_diagonal_right_down_check_result == True:
                        hit_count = hit_count + 1
                    elif m_diagonal_right_up_check_result == True and s_diagonal_left_down_check_result == True and m_diagonal_left_up_check_result == True and s_diagonal_right_down_check_result == True:
                        hit_count = hit_count + 1
                    elif s_diagonal_right_up_check_result == True and m_diagonal_left_down_check_result == True and m_diagonal_left_up_check_result == True and s_diagonal_right_down_check_result == True:
                        hit_count = hit_count + 1
                    elif m_diagonal_right_up_check_result == True and s_diagonal_left_down_check_result == True and s_diagonal_left_up_check_result == True and m_diagonal_right_down_check_result == True:
                        hit_count = hit_count + 1
                    else:
                        print("No hits identified!")
    print("Final hit count: ",hit_count)
    return hit_count

def main():
    input_data = read_file(FILE_PATH)
    output = xmas_checker(input_data)

if __name__ == "__main__":
    main()