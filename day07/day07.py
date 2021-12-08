from matplotlib import pyplot as plt

def plot_cost(in_lst):
    a = set(in_lst)
    x = range(min(a), max(a) + 1)
    y = [calc_cost_2(index, in_lst) for index in x]
    plt.plot(x, y)
    plt.show()

def calc_cost(final_pos, horz_vector):
    return sum([abs(final_pos-pos) for pos in horz_vector])

def calc_cost_2(final_pos, horz_vector):
    return sum([sum(range(1,abs(final_pos-pos)+1)) for pos in horz_vector])

def find_minimum(index, in_lst, min_fcn_version):
    current_cost = min_fcn_version(index, in_lst)
    next_index_cost = min_fcn_version(index + 1, in_lst)
    
    search_dir = -1 if current_cost < next_index_cost else 1
    prev_cost = current_cost
    while prev_cost >= current_cost:
        index += search_dir
        prev_cost  = current_cost
        current_cost = min_fcn_version(index, in_lst)
    return (index + search_dir, prev_cost)


if __name__=='__main__':
    with open("day07/input.txt") as f:
        input_lst = list(map(int, f.readlines()[0].split(',')))
    
    # Make a good initial guess
    input_lst.sort()
    init = input_lst[int(len(input_lst)/2)]

    print("Part1: Optimal position at %d, with the cost %d" % find_minimum(init, input_lst, calc_cost))
    print("Part2: Optimal position at %d, with the cost %d" % find_minimum(init, input_lst, calc_cost_2))

