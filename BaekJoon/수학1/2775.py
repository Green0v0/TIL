import sys
T = int(sys.stdin.readline().rstrip())

for idx in range(T):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    zero_floor = [i+1 for i in range(n)]
    floor = []
    for i in range(k):
        if i == 0:
            a = 0
            for j in range(n):
                a += zero_floor[j]
                floor.append(a)
        else:
            a = 0
            for j in range(n):
                a += floor[j]
                floor[j] = a
        # print(f'{i}번째{floor}')
    print(floor[n-1])

# 다른 풀이 1
Case = input()
for _ in range(int(Case)):
    k = int(input())
    n = int(input())
    num = [i for i in range(1, n + 1)]
    for _ in range(k):
        for j in range(1, n):
            num[j] += num[j-1]
    print(num[-1])
