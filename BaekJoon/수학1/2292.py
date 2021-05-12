import sys
N = int(sys.stdin.readline().rstrip())
# 시간, 메모리 초과
# results = [2 + (3*x*(x-1)) for x in range(1,N//4) if 2 + (3*x*(x-1))<=N]
# print(len(results)+1)

# 성공 풀이
y = 0
while True :
# while N < 100000001: 가능
    if N == 1:
        y = 1
        break
    elif N - (1 + (3*y*(y-1))) <= 0:
        break
    else:
        y += 1
print(y)
