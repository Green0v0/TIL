import sys
tmp = 0
li = list(range(1,21))
for i in range(10):
    a, b = map(int, sys.stdin.readline().split())
    # 인덱스는 0부터 시작
    a = a-1
    b = b-1
    for _ in range((b-a+1)//2):
        tmp = li[a]
        li[a] = li[b]
        li[b] = tmp
        a += 1
        b -= 1

print(*li)