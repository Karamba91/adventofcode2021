import time
#day04

def winning_bingo(no, bingo_boards):
    drawn_no = []
    winning_board = []
    for i in no:
        drawn_no.append(i)
        for board in bingo_boards:
            if (any([len(row) == len(set(row).intersection(drawn_no)) for row in board[0]]) or
                any([len(col) == len(set(col).intersection(drawn_no)) for col in board[1]])):
                winning_board = board[0]
                break
        if winning_board != []:
            break
    board_set = set()
    for row in winning_board:
        board_set.update(set(row))
    board_set.difference_update(drawn_no)
    last_draw = int(drawn_no[-1])
    sum_unselect = sum(map(int,board_set))
    return last_draw, sum_unselect, last_draw*sum_unselect

def last_winning_bingo(no, bingo_boards):
    drawn_no = no
    last_winning_board = []
    for i in range(len(no)-1, -1, -1):
        drawn_no = no[:i]
        for board in bingo_boards:
            if not (any([len(row) == len(set(row).intersection(drawn_no)) for row in board[0]]) or
                any([len(col) == len(set(col).intersection(drawn_no)) for col in board[1]])):
                last_winning_board = board[0]
                break
        if last_winning_board != []:
            break
    board_set = set()
    for row in last_winning_board:
        board_set.update(set(row))
    board_set.difference_update(drawn_no+[no[i]])
    last_draw = int(no[i])
    sum_unselect = sum(map(int,board_set))
    return last_draw, sum_unselect, last_draw*sum_unselect

def fix_input(in_lst):
    bingo_number = list(input_lst[0].split(','))
    bing_board = list(map(str.split, input_lst[1:]))
    all_boards = []
    new_board = []
    for row in bing_board[1:]:
        if row == []:
            all_boards.append((new_board, list(map(list, zip(*new_board)))))
            new_board=[]
            continue
        new_board.append(row)
    return bingo_number, all_boards
        
    

if __name__=='__main__':
    with open("day04/input.txt") as f:
        input_lst = list(map(str.strip, f.readlines()))
        bingo_no, rows_cols = fix_input(input_lst)
        start_time =  time.time()
        a, b, c = winning_bingo(bingo_no, rows_cols)
        finish_time = str(time.time() - start_time)
        print("First winning\nLast draw: %s sum of unselected: %s \nProduct: %s\nTime to execute: %s" % (a,b,c,finish_time))
        
        start_time =  time.time()
        a, b, c = last_winning_bingo(bingo_no, rows_cols)
        finish_time = str(time.time() - start_time)
        print("Last winning\nLast draw: %s sum of unselected: %s \nProduct: %s\nTime to execute: %s" % (a,b,c,finish_time))
