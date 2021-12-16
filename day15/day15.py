def get_adjecent_nodes(coord, max_x, max_y):
    all_adj = [(coord[0]-1, coord[1]), (coord[0]+1, coord[1]),(coord[0], coord[1]-1),(coord[0], coord[1]+1)]
    return list(filter(lambda x: ((x[0] >= 0) and (x[0] < max_x) and (x[1] >= 0) and (x[1] < max_y)), all_adj))

def get_value(in_map, coord):
    return int(in_map[coord[1]][coord[0]])

def get_all_nodes(in_map):
    return [(x, y) for y in range(len(in_map)) for x in range(len(in_map[0]))]

def djikstra_algorithm(graph, start_node):
    unvisited = list(get_all_nodes(graph))
    shortest_path = {}
    previous = {}
    max_value = 5000000000
    for node in unvisited:
        shortest_path[node] = max_value
    shortest_path[start_node] = 0
    
    while unvisited:
        current_min_node = None
        for node in unvisited:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        adjecent_nodes = get_adjecent_nodes(current_min_node, len(graph), len(graph[0]))
        for next_node in adjecent_nodes:
            temp = shortest_path[current_min_node] + get_value(graph, next_node)
            if temp < shortest_path[next_node]:
                shortest_path[next_node] = temp
                previous[next_node] = current_min_node
        unvisited.remove(current_min_node)
    return previous, shortest_path

def a_star_algorithm(start, goal,):
    return False

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(str(node)+", ")
        node = previous_nodes[node]

 
    # Add the start node manually
    path.append(str(start_node))
    
    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))

def make_five_times(in_map):
    temp  = [list(map(int,row)) + [(int(el)+1)%10 for el in row] + [(int(el)+2)%10 for el in row]  +
                [(int(el)+3)%10 for el in row] + [(int(el)+4)%10 for el in row] for row in in_map]
    ret_lst = temp.copy()
    for i in range(1,5):
        for row in temp:
            ret_lst.append([(el + i)%10 for el in row])
    return ret_lst

if __name__=='__main__':
    with open("day15/test_input.txt") as f:
        input_lst = list(map(str.strip, f.readlines()))
    
    #p, s = djikstra_algorithm(input_lst,(0,0))
    #print_result(p, s, (0,0), (len(input_lst)-1, len(input_lst[0])-1))

    larger_map = make_five_times(input_lst)
    p, s = djikstra_algorithm(larger_map,(0,0))
    print_result(p, s, (0,0), (len(larger_map)-1, len(larger_map[0])-1))
