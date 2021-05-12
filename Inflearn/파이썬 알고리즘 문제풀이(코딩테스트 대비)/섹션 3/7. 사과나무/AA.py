import sys
N = int(sys.stdin.readline().rstrip())
li =[]
total = 0
for t in range(N):
    if t == 0:
        a = 1
    elif t <= N//2:
        a += 2
    else:
        a -= 2
    b = (N-a)//2
    li = list(map(int,sys.stdin.readline().split()))
    index = b
    for _ in range(a):
        total += li[index]
        index += 1

print(total)
