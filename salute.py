def solution(s):
    employees_r = []
    employees_l = []
    pos = 0
    rslt = 0
    for letter in s:
        if letter == ">":
            employees_r.append(pos)
        elif letter == "<":
            employees_l.append(pos)
        pos += 1

    for e_r in employees_r:
        for e_l in employees_l:
            if e_r < e_l:
                rslt += 2

    return rslt

if __name__ == "__main__":
    print(solution(">----<"))
    print(solution("<<>><"))
    print(solution("--->-><-><-->-"))