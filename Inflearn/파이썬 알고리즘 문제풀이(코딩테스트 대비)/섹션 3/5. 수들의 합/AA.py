import sys

N,M = map(int,sys.stdin.readline().split())
li = list(map(int,sys.stdin.readline().split()))

cnt = 0
# print(li[0:3])
# [1, 2, 1]
for i in range(1,len(li)+1):
    if li[i-1] == M:
        cnt += 1
    for j in range(len(li)):
        if j+i+1 > len(li):
            break
        # print(f'i : {i} j : {j} j+i+1 : {j+i+1} sum(li[j:j+i+1] : {sum(li[j:j+i+1])}')
        if sum(li[j:j+i+1]) == M:
            cnt+=1
print(cnt)