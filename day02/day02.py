import re

def calc_pos(dir_lst):
    vert = 0
    horiz = 0
    for instruction in dir_lst:
        match_result = re.match('(\w+) (\d+)', instruction).groups()
        if 'down' == match_result[0]:
            vert += int(match_result[1])
        elif 'up' == match_result[0]:
            vert -= int(match_result[1])
        elif 'forward' == match_result[0]:
            horiz += int(match_result[1])
        
    return vert * horiz

def calc_pos_2(dir_lst):
    aim = 0
    vert = 0
    horiz = 0
    for instruction in dir_lst:
        match_result = re.match('(\w+) (\d+)', instruction).groups()
        if 'down' == match_result[0]:
            aim += int(match_result[1])
        elif 'up' == match_result[0]:
            aim -= int(match_result[1])
        elif 'forward' == match_result[0]:
            horiz += int(match_result[1])
            vert += int(match_result[1])*aim
        
    return vert * horiz

if __name__=='__main__':
    with open("day02/input.txt") as f:
        input_lst = list(map(str.strip, f.readlines()))
        print("Product of horiz. and vert. pos: " + str(calc_pos(input_lst)))
        print("New product of horiz. and vert. pos: " + str(calc_pos_2(input_lst)))