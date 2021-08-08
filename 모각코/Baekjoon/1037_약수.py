import sys
n = int(sys.stdin.readline().rstrip())
truely = list(map(int,sys.stdin.readline().split()))
mi, ma = min(truely), max(truely)
print(mi * ma)