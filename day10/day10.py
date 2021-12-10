valid_chunk = {'(': ')', '[': ']', '{':'}', '<':'>'}

def find_corrupted(first, remainder):
    if first in valid_chunk.keys():
        if len(remainder) == 1:
            return remainder
        remainder = find_corrupted(remainder[0], remainder[1:])
        if remainder == False:
            return False
        elif valid_chunk[first] == remainder[0]:
            if len(remainder) == 1:
                return True
            else:
                return remainder[1:]
        elif remainder[0] in valid_chunk.keys():
            
        else:
            return False 
    else:
        return first + remainder


    
    
        


if __name__=='__main__':
    with open("day10/input.txt") as f:
        input_lst = list(map(str.strip, f.readlines()))
    print(find_corrupted('(', '[(()())])'))