def create_age_list(all_fish):
    return_lst = [0]*9
    for x in set(all_fish):
        return_lst[x] += all_fish.count(x)
    return return_lst


def simulate_population(init, s_time):
    age_lst = create_age_list(init)
    for _ in range(s_time):
        age_lst = age_lst[1:] + [age_lst[0]]
        age_lst[6] += age_lst[-1]
    return sum(age_lst)


if __name__=='__main__':
    with open("day06/input.txt") as f:
        input_lst = list(map(int, f.readlines()[0].split(',')))
    print("Pop. after 80 days: %d" % simulate_population(input_lst, 80))
    print("Pop. after 256 days: %d" % simulate_population(input_lst, 256))