import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    blank, star = i, n - i
    print(' ' * blank + '*' * star)
