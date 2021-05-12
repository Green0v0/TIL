import sys
n = int(input())
su=list(map(int,input().split()))
li=[n+1]*n
cnt=0 #자신보다 높은 수의 갯수
# print(li)
point=0 #인덱스 포인트
for i in range(n):
    point=su[i]
    # i=0 <- 1번째 su[i]=5
    while cnt != su[i]:
        cnt=0
        for j in range(point):
            if li[j]>i+1:
                cnt+=1
        if cnt!=su[i]:
            point+=1
    if li[point]==n+1:
        li[point]=i+1
    else:
        while li[point]!=n+1:
            point+=1
        li[point]=i+1
    print(li)
print(li)