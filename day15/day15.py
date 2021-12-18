from queue import PriorityQueue

def get_adjecent_nodes(coord, max_x, max_y):
    all_adj = [(coord[0]-1, coord[1]), (coord[0]+1, coord[1]),(coord[0], coord[1]-1),(coord[0], coord[1]+1)]
    return list(filter(lambda x: ((x[0] >= 0) and (x[0] < max_x) and (x[1] >= 0) and (x[1] < max_y)), all_adj))

def get_value(in_map, coord):
    return int(in_map[coord[1]][coord[0]])

def get_all_nodes(in_map):
    return [(x, y) for y in range(len(in_map)) for x in range(len(in_map[0]))]

def search_cheap(graph, start_node):
    unvisited = set(get_all_nodes(graph))
    queue = PriorityQueue()
    shortest_path = {}
    previous = {}
    
    max_value = float('inf')
    for node in unvisited:
        shortest_path[node] = max_value
    shortest_path[start_node] = 0
    queue.put((0, start_node))
    
    while unvisited:
        current_node = queue.get()[1]

        adjecent_nodes = get_adjecent_nodes(current_node, len(graph), len(graph[0]))
        for next_node in adjecent_nodes:
            temp = shortest_path[current_node] + get_value(graph, next_node)
            if temp < shortest_path[next_node]:
                shortest_path[next_node] = temp
                previous[next_node] = current_node
                queue.put((temp ,next_node))
        unvisited.remove(current_node)
        
    return previous, shortest_path

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(str(node)+", ")
        node = previous_nodes[node]

    print("We found the following best path with a value of {}".format(shortest_path[target_node]))


def make_five_times(in_map):
    temp  = [increment_block(row,0) + increment_block(row,1) + increment_block(row,2)  +
                increment_block(row,3) + increment_block(row,4) for row in in_map ]
    ret_lst = temp.copy()
    for i in range(1,5):
        for row in temp:
            ret_lst.append(increment_block(row, i))
    return ret_lst

def increment_block(block, incre):
    ret_lst = list()
    for el in block:
        if int(el) + incre < 10:
            ret_lst += [(int(el)+incre)%10]
        else:
            ret_lst += [(int(el)+incre)%10 + 1]
    return ret_lst

if __name__=='__main__':
    with open("day15/input.txt") as f:
        input_lst = list(map(str.strip, f.readlines()))
    
    p, s = search_cheap(input_lst,(0,0))
    print_result(p, s, (0,0), (len(input_lst)-1, len(input_lst[0])-1))

    larger_map = make_five_times(input_lst)
    p, s = search_cheap(larger_map,(0,0))
    print_result(p, s, (0,0), (len(larger_map)-1, len(larger_map[0])-1))
