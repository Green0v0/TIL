from itertools import permutations
def solution(numbers):
    num = list(numbers)
    answer_li = []
    cnt = 0
    for i in range(len(num)):
        for c in list(permutations(num, i+1)):
            word = ''.join(c)
            answer_li.append(word)
    new_li = list(set(map(int,answer_li)))
    for nl in new_li:
        if nl <= 1:
            continue
        for x in range(2,int(nl**(1/2))+1):
            if nl % x == 0:
                break
        else:
            cnt += 1
    print(cnt)
print(solution('17'))
print(solution('011'))

# 다른 사람 풀이
from itertools import permutations
def solution1(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)