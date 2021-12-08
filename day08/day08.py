
def count_no(in_list):
    tot_sum = 0
    for row in map(lambda x: x.split(' | ')[1].split(' '), in_list):
        tot_sum += sum([1 for digit in row if len(digit) in [2,3,4,7]])
    return tot_sum

def count_all(in_list):
    tot_sum = 0
    for row in map(lambda x: x.split(' | '), in_list):
        digits = get_digits(row[0].split(' '))
        new_value = int("".join([ match_index(digits, digit) for digit in row[1].split(' ')]))
        tot_sum += new_value
    return tot_sum

def match_index(digits, dig):
    true_false_lst = list(map(lambda x: len(set(x).symmetric_difference(dig)) == 0, digits))
    return str(true_false_lst.index(True))
    
        
def get_digits(digits):
    digits_lst = [None]*10
    for dig in digits:
        if len(dig) == 2:
            digits_lst[1] = dig
        elif len(dig) == 3:
            digits_lst[7] = dig
        elif len(dig) == 4:
            digits_lst[4] = dig
        elif len(dig) == 7:
            digits_lst[8] = dig

    for dig in digits:
        if (len(dig) == 6) and (len(set(dig)&set(digits_lst[1])) == 1):
            digits_lst[6] = dig
        elif (len(dig) == 6) and (len(set(dig)&set(digits_lst[4])) == 4):
            digits_lst[9] = dig
        elif len(dig) == 6:
            digits_lst[0] = dig
        elif (len(dig) == 5) and (len(set(dig) & set(digits_lst[1])) == 2):
            digits_lst[3] = dig
        elif (len(dig) == 5) and (len(set(dig) - set(digits_lst[4]))==2):
            digits_lst[5] = dig
        elif (len(dig) == 5):
            digits_lst[2] = dig
    
    return digits_lst





if __name__=='__main__':
    with open("day08/input.txt") as f:
        input_lst = list(map(str.strip, f.readlines()))
    result_1 = count_no(input_lst)
    print('Total sum of 1,4,7,8 is %d' % result_1)
    result_2 = count_all(input_lst)
    print ("Total sum of encoded data is %d" % result_2)
