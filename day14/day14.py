
def create_smart_polymer(init, conversion, sim_step):
    conv_dict = create_conversion_dict(conversion)
    poly_pair = list(map(lambda x: x[0]+x[1],zip(init[:-1], init[1:])))
    poly_count = {k:0 for k in conv_dict.keys()}
    for i in set(poly_pair):
        poly_count[i] += poly_pair.count(i)
    
    for _ in range(sim_step):
        next_loop = {k:0 for k in conv_dict.keys()}
        for k in poly_count.keys():
                if poly_count[k] != 0:
                    next_loop[conv_dict[k][0]] = (next_loop[conv_dict[k][0]] + poly_count[k])
                    next_loop[conv_dict[k][1]] = (next_loop[conv_dict[k][1]] + poly_count[k])
        poly_count = next_loop
    
    elem_counter = dict()
    last_pair = init[:2]
    for _ in range(sim_step):
        last_pair = conv_dict[last_pair][0]
    elem_counter[last_pair[0]] = 1
    for i in poly_count.keys():
        if i[-1] in elem_counter.keys():
            elem_counter[i[-1]] += poly_count[i]
        else:
            elem_counter[i[-1]] = poly_count[i]

    return elem_counter


def create_conversion_dict(conversions):
    conv = map(lambda x: tuple(x.split(' -> ')), conversions)
    return {k:[k[0]+v,v+k[1]] for k,v in conv}

def find_most_least_common(elem_list):
    return (elem_list[max(elem_list.keys(), key=lambda k: elem_list[k])], 
           elem_list[min(elem_list.keys(), key=lambda k: elem_list[k])])

if __name__=='__main__':
    with open("day14/input.txt") as f:
        input_lst = list(map(str.strip, f.readlines()))
    init_polymer = input_lst[0]
    conversion = input_lst[2:]

    polymer = create_smart_polymer(init_polymer, conversion, 10)
    p_max, p_min = find_most_least_common(polymer)
    print("Diff between most and least common %d" % (p_max-p_min))

    polymer = create_smart_polymer(init_polymer, conversion, 40)
    p_max, p_min = find_most_least_common(polymer)
    print("Diff between most and least common %d" % (p_max-p_min))
