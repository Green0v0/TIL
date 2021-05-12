import sys

# sort 와 sorted의 차이
# https://inma.tistory.com/137

N = int(sys.stdin.readline().rstrip())
N_li = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
M_li = list(map(int,sys.stdin.readline().split()))
#
# NM = N_li+M_li
# print(*sorted(NM))

c = []
p1 = 0
p2 = 0
# or라서 안되는 이유 기억하기
while (p1 != N) and (p2 != M):
    if N_li[p1] <= M_li[p2]:
        c.append(N_li[p1])
        p1 += 1
    else:
        c.append(M_li[p2])
        p2 += 1
if p1 == N:
    c = c + M_li[p2:]
else:
    c = c + N_li[p1:]
print(*c)
# or (p2 != M)