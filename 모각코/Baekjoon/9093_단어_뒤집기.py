import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    s = list(map(lambda x: x[::-1],sys.stdin.readline().split()))
    print(' '.join(s))