import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    blank, star = n - i - 1, i + 1
    result = ' ' * blank + '*' * star
    if i > 0:
        result += '*' * i
    print(result)
for j in range(n - 1):
    blank, star = j, n - j - 1
    result = ' ' + ' ' * blank + '*' * star
    if j < n - 1:
        result += '*' * (star - 1)
    print(result)