import re

def transpose(sheet, instruction):
    fold = re.search(r"([x-y])=(\d+)", instruction).groups()
    return_set = set()
    for point in sheet:
        fold_num = int(fold[1])
        if fold[0] == 'x' and point[0] > fold_num:
            diff = point[0]-fold_num
            if fold_num-diff >= 0:
                return_set.update([(fold_num-diff, point[1])])
        elif fold[0] == 'y' and point[1]> fold_num:
            diff = point[1]-fold_num
            if fold_num-diff >= 0:
                return_set.update([(point[0], fold_num-diff)])
        else:
            return_set.update([point])
    return return_set

def fold_all(sheet, instructions):
    for inst in instructions:
        sheet = transpose(sheet, inst)
    return sheet

def print_sheet(sheet):
    max_x = 40
    max_y = 10
    print('\n'.join([''.join(['#' if (x,y) in sheet else '.' for x in range(max_x + 1)]) for y in range(max_y + 1)]))

def create_sheet(input_lst):
    sheet = set()
    for i, dot in enumerate(input_lst):
        if dot == '':
            return input_lst[i+1:], sheet
        sheet.update([(int(dot.split(',')[0]), int(dot.split(',')[1]))])


if __name__=='__main__':
    with open("day13/input.txt") as f:
        input_lst = list(map(str.strip, f.readlines()))
    print(input_lst)
    instructions,  sheet  = create_sheet(input_lst)
    print("Sheet is " + str(sheet))
    print("Instructions: %s" % instructions)
    print("Number of dots: %s" % len(transpose(sheet, instructions[0])))

    sheet = fold_all(sheet, instructions)
    print_sheet(sheet)