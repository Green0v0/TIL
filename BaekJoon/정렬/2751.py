import sys
N = int(sys.stdin.readline().rstrip())
li = []
for _ in range(N):
    li.append(int(sys.stdin.readline().rstrip()))

li.sort()
for i in range(N):
    print(li[i])