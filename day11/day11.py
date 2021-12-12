from itertools import product, chain

def is_valid(coord,  x_oob, y_oob):
    return (coord[0] < x_oob and coord[0] >= 0 and coord[1] < y_oob and coord[1] >= 0)

def get_adjacent_coords(coord, y_oob, x_oob):
    x_lst, y_list = [coord[0]-1, coord[0], coord[0]+1], [coord[1]-1, coord[1], coord[1]+1]
    coords = list(product(x_lst, y_list))
    coords.remove(coord)
    ret = list(filter(lambda x: is_valid(x, x_oob, y_oob), coords))
    return ret

def charge_all(map_lst):
    return [list(map(lambda x: x + 1, row)) for row in map_lst]

def charge_flash(map_lst, coords):
    return_lst = []
    for y, row in enumerate(map_lst):
        temp =[]
        for x, p in enumerate(row):
            if (x, y) in coords:
                if p != 0:
                    temp += [p + 1]
                else:
                    temp += [0]
            else:
                temp += [p]
        return_lst += [temp]
    return return_lst

def find_full_energy(input_lst):
    return [(x, y) for y, row in enumerate(input_lst) for x, p in enumerate(row) if p > 9]

def flash(map_lst):
    flash_coord = set()
    to_flash = set(find_full_energy(map_lst))
    while len(to_flash) != 0:
        coord = to_flash.pop()
        flash_coord.update([coord])
        map_lst[coord[1]][coord[0]] = 0
        gac =  get_adjacent_coords(coord, len(map_lst), len(map_lst[0]))
        map_lst = charge_flash(map_lst, gac)
        to_flash.update(set(find_full_energy(map_lst)))
    return map_lst, len(flash_coord)

def simulate(map_lst, iteration):
    flashes = 0
    for i in range(iteration):
        map_lst = charge_all(map_lst)
        map_lst, no_flash = flash(map_lst)
        flashes += no_flash
    return flashes

def all_flash(map_lst):
    iteration = 0
    while True:
        if all(map(all, [map(lambda x: x == 0, row) for row in map_lst])):
            break
        map_lst = charge_all(map_lst)
        map_lst, _ = flash(map_lst)
        iteration += 1
    return iteration


def print_matrix(map_lst, iteration):
    print("After step %d", iteration)
    print( "\n".join(["".join(map(str, row)) for row in map_lst]))

if __name__=='__main__':
    with open("day11/input.txt") as f:
        input_lst = list(map(str.strip, f.readlines()))
    int_array = [[int(point) for point in row] for row in input_lst ]
    print("Number of flashes after 100 steps %d" % simulate(int_array,100))
    print("At iteration %d will all flash" % all_flash(int_array))