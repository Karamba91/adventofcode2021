operator = {0: '+', 1: '*', 2: 'min', 3: 'max', 5: '>', 6: '<', 7: '==' }

def convert_to_bin(init):
    lst = ""
    for hex_num in init:
        lst += "{0:04b}".format((int(hex_num,16)))
    return lst

def analyze(bin_str):
    version_sum = 0
    result = []
    bits = []
    packets = []
    while len(bin_str) >= 11:
        version, type_id, bin_str = int(bin_str[:3], 2), int(bin_str[3:6], 2), bin_str[6:]
        version_sum += version
        if not any(map(lambda x: x=='1',bin_str)):
            break
        if type_id == 4:
            lit, bin_str, tot_bits = literal(bin_str)
            result += [(6+tot_bits,'lit', lit)]
        else:
            length_type_id, bin_str = bin_str[0], bin_str[1:]
            if int(length_type_id):
                sub_pack, bin_str = int(bin_str[:11], 2), bin_str[11:]
                packets += [sub_pack]
                result += [(6+1+11, 'Sub packets', sub_pack, operator[type_id])]
            else:
                sub_bit, bin_str = int(bin_str[:15], 2), bin_str[15:]
                bits += [sub_bit]
                result += [(6+1+15, 'Packet bits', sub_bit,operator[type_id])]

    return result

def literal(bin_str):
    literal =''
    tot_bits = 0
    while True:
        tot_bits += 5
        if bin_str[0] == '1':
            literal += bin_str[1:5]
            bin_str = bin_str[5:]
        else:
            literal += bin_str[1:5]
            return int(literal, 2), bin_str[5:], tot_bits

def eval_expression(lst):
    if lst[0][1] == 'Packet bits':
        sum_bit = 0
        for index, tup in enumerate(lst[1:]):
            sum_bit += tup[0]
            if sum_bit == lst[0][2]:
                if (lst[0][3] == 'max') or (lst[0][3] == 'min'):
                    return [eval(lst[0][3] +'({})'.format(str(list(map(str, eval_expression(lst[1:index+1+1]))))))]
                else:
                    return [int(eval(lst[0][3].join(map(str, eval_expression(lst[1:index+1+1])))))]
    elif lst[0][1] == 'Sub packets':
        if (lst[0][3] == 'max') or (lst[0][3] == 'min'):
            return [eval(lst[0][3] +'({})'.format(str(list(map(str, eval_expression(lst[1:(int(lst[0][2]) + 1)]))))))]
        else:
            return [int(eval(lst[0][3].join(map(str, eval_expression(lst[1:(int(lst[0][2]) + 1)])))))]
    elif lst[0][1] == 'lit' and len(lst) > 1:
        return [lst[0][2]] + eval_expression(lst[1:])
    elif lst[0][1] == 'lit':
        return [lst[0][2]]
    
    


if __name__=='__main__':
    with open("day16/input.txt") as f:
        input_lst = list(map(str.strip, f.readlines()))
    # series = analyze(convert_to_bin(input_lst[0]))
    series = analyze(convert_to_bin("9C0141080250320F1802104A08"))
    print(series)
    res = eval_expression(series)[0]
    print(res)
    #print(analyze(convert_to_bin("880086C3E88112")))
