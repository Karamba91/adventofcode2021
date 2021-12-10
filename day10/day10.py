valid_chunk = {'(': ')', '[': ']', '{':'}', '<':'>'}
syntax_score_dict = {None: 0, ')':3, ']':57, '}':1197, '>': 25137}
complete_score_dict = {None: 0, ')':1, ']':2, '}':3, '>':4}

def find_problem(line, syntax_check=True):
    expected_lst = []
    for sign in line:
        if sign in valid_chunk.keys():
            expected_lst.append(valid_chunk[sign])
        else:
            expected = expected_lst.pop()
            if sign != expected and syntax_check:
                return sign
            elif (sign != expected) and not syntax_check:
                return []
                #raise ValueError("Got %s expected %s" % (sign, expected))
    if syntax_check == False:
        expected_lst.reverse()
        return expected_lst


def syntax_error_score(code):   
    return sum([syntax_score_dict[find_problem(line)] for line in code])

def autocomplete_score(code):
    scores = []
    for line in code:
        score = 0
        for sign in find_problem(line, False):
            score = (5 * score) + complete_score_dict[sign]
        scores += [score] if score > 0 else []
    scores.sort()
    return scores


if __name__=='__main__':
    with open("day10/input.txt") as f:
        input_lst = list(map(str.strip, f.readlines()))
    print("Syntax error score is %d" % syntax_error_score(input_lst))
    cmp_score = autocomplete_score(input_lst)
    print("Autocomplete score is %d" % cmp_score[int(len(cmp_score)/2)])