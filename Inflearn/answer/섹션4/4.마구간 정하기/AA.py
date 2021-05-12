import sys
n, c = map(int,sys.stdin.readline().split())
n_list=[]
for _ in range(n):
    n_list.append(int(sys.stdin.readline().rstrip()))
    n_list.sort()
def Count(mid):
    res=1; cnt=1
    for x in n_list:
        if x>=res+mid:
            cnt += 1
            res += mid
    return cnt
lt=0
rt=n-1
while lt<=rt:
    mid=(lt+rt)//2
    if mid==1:
        break
    elif Count(mid)<=c:
        rt=mid-1
    # 거리 조건 추가해야함
    else:
        lt=mid+1
# print(Count(mid),mid)