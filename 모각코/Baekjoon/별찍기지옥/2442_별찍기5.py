import sys
n = int(sys.stdin.readline().rstrip())
# 1 + 2 * (n - 1)개 까지
for i in range(n):
    blank, star = n - i - 1, i + 1
    result = ' ' * blank + '*' * star
    if i > 0:
        result += '*' * i
    print(result)