def check_horizontal_vertical(vector):
    return (vector[0][0] == vector[1][0] or vector[0][1] == vector[1][1])

def find_horizontal_vertical(input_lst):
    return filter(check_horizontal_vertical, input_lst)

def linspace(start, end):
    return range(start, end - 1, -1) if start > end else range(start, end + 1)

def visited_coord(h_v_vectors):
    visited = set()
    multiple = set()
    for vector in h_v_vectors:
        if vector[1][1]-vector[0][1] == 0:
            temp = list(zip(linspace(vector[0][0], vector[1][0]), [vector[0][1]]*int(abs(vector[1][0]-vector[0][0])+1)))
        elif vector[1][0]-vector[0][0] == 0:
            temp = list(zip([vector[0][0]]*int(abs(vector[1][1]-vector[0][1])+1), linspace(vector[0][1], vector[1][1])))
        else:
            temp = list(zip(linspace(vector[0][0], vector[1][0]), linspace(vector[0][1], vector[1][1])))
        multiple.update(visited.intersection(temp))
        visited.update(temp)

    return multiple
    

if __name__=='__main__':
    with open("day05/input.txt") as f:
        input_lst = tuple(map(str.strip, f.readlines()))
        refined_input = list(map(lambda x: tuple(map(
            lambda y: tuple(map(int, y.split(','))), x.split(' -> '))), input_lst))
        h_v_vectors = find_horizontal_vertical(refined_input)
        multi = visited_coord(h_v_vectors)
        print(len(multi))
        multi2 = visited_coord(refined_input)
        print(len(multi2))
        
