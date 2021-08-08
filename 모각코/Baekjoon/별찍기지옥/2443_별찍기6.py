import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    blank, star = i, n - i
    result = ' ' * blank + '*' * star
    if i < n - 1:
        result += '*' * (star - 1)
    print(result)