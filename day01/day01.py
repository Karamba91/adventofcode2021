def no_deeper(depths):
    return sum([depths[i] < depths[i+1] for i in range(len(depths)-1)])

def three_average(depths):
    return no_deeper([depths[i-2] + depths[i-1] + depths[i] for i in range(2, len(depths))])

if __name__=='__main__':
    with open("day01/input.txt") as f:
        input_lst = list(map(int, f.readlines()))
        print("Number of deeper: " + str(no_deeper(input_lst)))
        print("Number of deeper 3-avg: " + str(three_average(input_lst)))
