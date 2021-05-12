import sys
n = int(sys.stdin.readline().rstrip())
li=[]
for _ in range(n):
    h,w = map(int,sys.stdin.readline().split())
    li.append((h,w))
cnt=0
# for i in range(n):
#     for j in range(n):
        # 만약 조건을 만족하는 대상이 하나 더 있으면 1개 더 카운트 되서 wrong answer
        # if li[i][0] < li[j][0]:
        #     if li[i][1] < li[j][1]:
        #         cnt+=1

li.sort(key=lambda x : x[0])
# print(li)
for i in range(n):
    if any(li[i][1]<li[k][1] for k in range(i,n)):
        cnt+=1
print(n-cnt)