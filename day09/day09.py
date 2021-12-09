def low_point_sum(in_map):
    low_points = []
    for y, row in enumerate(in_map):
        for x, point in enumerate(row):
            new_coord = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            new_f_coord = [c for c in new_coord if not not_valid(c, len(row)-1, len(in_map)-1)]
            if all([point < in_map[x[1]][x[0]] for x in new_f_coord]):
                low_points += [point]        
    return low_points

def find_basins(in_map):
    visited = set()
    basins = list()
    for y, row in enumerate(in_map):
        for x, point in enumerate(row):
            if point == '9' or ((x,y) in visited):
                visited.update((x,y))
                continue
            unexplored = set([(x,y)])
            basin = set()
            while len(unexplored) != 0:
                check_coord = unexplored.pop()
                if (check_coord in visited) or (check_coord in basin) or (in_map[check_coord[1]][check_coord[0]] == '9'):
                    visited.update([check_coord])
                    continue
                new_coord = [(check_coord[0]-1, check_coord[1]), (check_coord[0]+1, check_coord[1]),
                                (check_coord[0], check_coord[1]-1), (check_coord[0], check_coord[1]+1)]
                unexplored.update([coord for coord in new_coord 
                                    if (coord not in visited) and (coord not in basin)
                                    and (not not_valid(coord, len(row)-1, len(in_map)-1))])
                visited.update([check_coord])
                basin.update([check_coord])
            basins += [basin]
    basins.sort()
    return basins

def not_valid(coord, max_x, max_y):
    return (coord[0] > max_x) or (coord[0] < 0) or (coord[1] > max_y) or (coord[1] < 0)

if __name__=='__main__':
    with open("day09/input.txt") as f:
        input_lst = list(map(str.strip, f.readlines()))
    result = low_point_sum(input_lst)
    print("Sum of risk at low points: %d" % sum(map(lambda x: int(x)+1, result)))
    basins = find_basins(input_lst)
    basins = list(map(len, basins))
    basins.sort()
    print("Multiplying the largest gives: %d" % (basins[-1]*basins[-2]*basins[-3]))
