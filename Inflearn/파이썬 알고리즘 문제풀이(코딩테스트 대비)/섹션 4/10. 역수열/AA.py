import sys
n = int(input())
su=list(map(int,input().split()))
li=[n+1]*n
# cnt=0 #자신보다 높은 수의 갯수
point=0 #인덱스 포인트
li2=[]
# print(li.count(8)) count사용 후 뒤에서부터 탐색
for i in range(n):
    point=su[i] #5
    for j in range(n):
        if j==n-1:
            li[li.index(n+1)]=i+1
            break
        li2=li[:-(j+1)]
        # print(li2)
        if li2.count(n+1)==point:
            li[-(j+1)]=i+1
            break

print(*li)
# for k in li:
#     print(k,end=' ')