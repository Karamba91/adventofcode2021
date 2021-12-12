def build_map(input_lst):
    cave_map = {}
    for connection in input_lst:
        result = connection.split('-')
        if result[0] in cave_map.keys():
            cave_map[result[0]] += [result[1]]
        else:
            cave_map[result[0]] = [result[1]]
        if result[1] in cave_map.keys():
            cave_map[result[1]] += [result[0]]
        else:
            cave_map[result[1]] = [result[0]]
    return cave_map

def first_small_multip(cave, path, visited_small_cave):
    if PART == 2:
        return (cave not in ["start", "end"]) and ((cave not in path) or ((path.count(cave) == 1) and not visited_small_cave))
    elif PART == 1:
        return (cave not in path)

def build_path(input_lst, part=1):
    cave_map = build_map(input_lst)
    paths = []
    paths_to_remove = []
    current_active_paths = set(['start'])
    while len(current_active_paths) != 0:
        active_at_start = current_active_paths.copy()
        for path in active_at_start:
            available_paths = cave_map[path.split(',')[-1]]
            visited_small_cave = any([path.count(c) > 1 for c in filter(str.islower, path.split(','))])
            for next_step in available_paths:
                if next_step == 'end':
                    paths += [path+","+next_step]
                elif next_step.islower() and first_small_multip(next_step, path,visited_small_cave):
                    current_active_paths.update([path+","+next_step])
                elif next_step.isupper():
                    current_active_paths.update([path+","+next_step])
            paths_to_remove +=[path]
        
        for remove_path in paths_to_remove:
            current_active_paths.remove(remove_path)
        paths_to_remove = []
    return paths, len(paths)


if __name__=='__main__':
    with open("day12/input.txt") as f:
        input_lst = list(map(str.strip, f.readlines()))
    PART = 1
    _, num_of_valid_paths = build_path(input_lst)
    print("Number of valid paths out of cave %d" % num_of_valid_paths)
    PART = 2
    _, num_of_valid_paths = build_path(input_lst)
    print("Number of valid paths out of cave %d" % num_of_valid_paths)