T = int(input())
sum = []
for i in range(T):
    a, b = map(int, input().split())
    sum.append(a+b)

for idx in range(T):
    print(sum[idx])

# 이게 안되는줄 알았는데 되나보네
cases = int(input())

for i in range(cases):
    a, b = map(int, input().split())
    print(a+b)