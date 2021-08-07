# dp - memoization
n = int(input())
memo = [0, 0] + [1] * (n - 1)

if n == 2:
    return memo[2]

for i in range(3, n + 1):
    memo[i] = memo[i-1] + 1