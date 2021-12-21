operator = {0: '+', 1: '*', 2: 'min', 3: 'max', 5: '>', 6: '<', 7: '=' }

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
            result += [('lit', lit, tot_bits + 6)]
        else:
            length_type_id, bin_str = bin_str[0], bin_str[1:]
            if int(length_type_id):
                sub_pack, bin_str = int(bin_str[:11], 2), bin_str[11:]
                packets += [sub_pack]
                result += [(operator[type_id], 'Sub packets', sub_pack)]
            else:
                sub_bit, bin_str = int(bin_str[:15], 2), bin_str[15:]
                bits += [sub_bit]
                result += [(operator[type_id], 'Packet bits', sub_bit)]

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



if __name__=='__main__':
    with open("day16/input.txt") as f:
        input_lst = list(map(str.strip, f.readlines()))
    print(analyze(convert_to_bin(input_lst[0])))
    #print(analyze(convert_to_bin("880086C3E88112")))




194