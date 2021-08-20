# min, max : X
import sys
sys.stdin = open("./input/input_2.txt", "r")

T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    target = list(map(int, input().split()))
    small = float('inf')
    large = float('-inf')
    for i in range(n - m + 1):
        value = sum(target[i : i + m])
        if value < small:
            small = value
        if large < value:
            large = value
    print(f'#{t + 1} {large - small}')
