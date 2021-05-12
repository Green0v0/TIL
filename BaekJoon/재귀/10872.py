import sys
N = int(sys.stdin.readline().rstrip())
factorial = 1
# 이렇게도 맞음
for i in range(1,N+1):
    factorial = factorial*i
print(factorial)

# 0에 대한 정의 추가
if N == 0:
    factorial = 1
else:
    for i in range(1, N + 1):
        factorial = factorial * i
print(factorial)