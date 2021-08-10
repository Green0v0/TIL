""" 3장 연속 run 3장 동일 triplet
9
111456
123123
233677
112233
333333
123456
667767
054060
101123
"""
from itertools import combinations
n = int(input())
for _ in range(n):
    origin = list(input())
    for com in list(combinations(origin,3)):
        s = origin[:]
        s.remove(com[0]); s.remove(com[1]); s.remove(com[2])
        com, s = sorted(list(map(int,com))), sorted(list(map(int,s)))
        if com[0] == com[1] == com[2] and s[0] + 2 == s[1] + 1 == s[2]:
            print('baby-gin')
            break
        elif com[0] + 2 == com[1] + 1 == com[2] and s[0] + 2 == s[1] + 1 == s[2]:
            print('baby-gin')
            break
        elif com[0] == com[1] == com[2] and s[0] == s[1] == s[2]:
            print('baby-gin')
            break
    else:
        print('NOT baby-gin')
