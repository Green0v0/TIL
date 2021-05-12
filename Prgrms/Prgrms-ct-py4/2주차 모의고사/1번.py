def solution1(seat):
    check = []
    for i in seat:
        if i not in check:
            check.append(i)
    return len(check)

def solution(seat):
    dict = {}

    for x,y in seat:
        dict[(x,y)] = 1

    return len(dict.keys())

print(solution([[1,1],[2,2],[3,3]]))
print(solution([[1,1],[2,1],[1,2],[3,4],[2,1],[2,1]]))