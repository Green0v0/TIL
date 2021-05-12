import sys
l=int(sys.stdin.readline().rstrip())
li=list(map(int,input().split()))
m=int(input())

# 가장 높은 곳에서 가장 낮은 곳으로 이동
li.sort(reverse=True)
for i in range(m):
    if li[0]<=li[1] or li[l-2]<=li[l-1]:
        li.sort(reverse=True)
    li[0]-=1
    li[l-1]+=1
print(max(li)-min(li))
