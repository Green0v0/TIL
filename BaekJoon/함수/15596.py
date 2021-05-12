# 정수 N개의 합
def solve(a):
    total = 0
    for i in range(len(a)):
        total = total + a[i]
    return total

a = [3, 2, 1]
print(solve(a))