def mean_bool(bool_list):
    transposed_list = map(list, zip(*bool_list))
    binary_str = "".join([max(set(col), key=col.count) for col in map(sorted, transposed_list)])
    return (int(binary_str, 2), int("".join(['0' if bit == '1' else '1' for bit in binary_str]), 2))

def o2_co2(bool_list):
    new_list = bool_list
    for i in range(len(bool_list[0])):
        transposed_list = list(map(list, zip(*new_list)))
        common = most(transposed_list[i], '1')
        new_list = list(filter(lambda x: x[i] == common, new_list))
        if len(new_list) == 1:
            break
    o2 = int(''.join(new_list), 2)

    new_list = bool_list
    for i in range(len(bool_list[0])):
        transposed_list = list(map(list, zip(*new_list)))
        common = most(transposed_list[i], '0')
        new_list = list(filter(lambda x: x[i] == common, new_list))
        if len(new_list) == 1:
            break
    co2 = int(''.join(new_list), 2)
    
    return o2 * co2

def most(in_list, default):
    ones = in_list.count('1')
    zeros = in_list.count('0')
    if default == '0':
        return '1' if (zeros > ones) else '0'
    else:
        return '1' if (ones >= zeros) else '0'

if __name__=='__main__':
    with open("day03/input.txt") as f:
        input_lst = list(map(str.strip, f.readlines()))
        gamma, epsilon = mean_bool(input_lst)
        print("Power consumption: " + str(gamma*epsilon))
        print("life support rating: " + str(o2_co2(input_lst)) )
