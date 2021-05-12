import sys
# sys.stdin = open("input.txt", "rt")

# N의 약수들 중 K번째로 작은 수를 출력
N , K = map(int,sys.stdin.readline().split())
li = []
try:
    for i in range(1,N+1):
        if N%i == 0:
            li.append(i)
        if len(li) > K-1 :
            break
    print(li[K - 1])
except:
    print(-1)

# 강의풀이
# 리스트를 사용하지 않음.
cnt = 0
for i in range(1,N+1):
    if N%i == 0:
       cnt += 1
    if cnt == K:
        print(i)
        break
else:
    print(-1)