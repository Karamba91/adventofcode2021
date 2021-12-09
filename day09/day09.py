def low_point_sum(in_map):
    low_points = []
    for y, row in enumerate(in_map):
        for x, point in enumerate(row):
            if (y == 0) and (x==0):
                if in_map[y+1][x] > point and row[x+1] > point:
                    low_points += [point]
            elif (y == 0) and (x==len(row)-1):
                if in_map[y+1][x] > point and row[x-1] > point:
                    low_points += [point]
            elif (y == len(in_map)-1) and (x == 0):
                if in_map[y-1][x] > point and row[x+1] > point:
                    low_points += [point]
            elif (y == len(in_map)-1) and (x==len(row)-1):
                if in_map[y-1][x] > point and row[x-1] > point:
                    low_points += [point]
            elif (y == 0):
                if all(map(lambda x: x > point, [in_map[y+1][x], row[x-1], row[x+1]])):
                    low_points += [point]
            elif (x == 0):
                if all(map(lambda x: x > point, [in_map[y+1][x], in_map[y-1][x], row[x+1]])):
                    low_points += [point]
            elif (x == len(row)-1):
                if all(map(lambda x: x > point, [in_map[y+1][x], in_map[y-1][x], row[x-1]])):
                    low_points += [point]
            elif (y == len(in_map)-1):
                if all(map(lambda x: x > point, [in_map[y-1][x], row[x-1], row[x+1]])):
                    low_points += [point]
            elif all(map(lambda x: x > point, [in_map[y-1][x], in_map[y+1][x], row[x-1], row[x+1]])):
                low_points += [point]
    return low_points

def find_basins(in_map):
    visited = set()
    basins = list()
    for y, row in enumerate(in_map):
        for x, point in enumerate(row):
            if point == '9':
                visited.update((x,y))
                continue
            elif (x,y) in visited:
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
                if (coord not in visited) and (coord not in basin) and (not not_valid(coord, len(row)-1, len(in_map)-1))])
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
    print(result)
    print(sum(map(lambda x: int(x)+1, result)))
    basins = find_basins(input_lst)
    basins = list(map(len, basins))
    basins.sort()
    print("Sizes of basins " + str(basins)) 
    print("Multiplying the largest gives: %d" % (basins[-1]*basins[-2]*basins[-3]))
