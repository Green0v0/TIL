n=6
times=[7,10]
# ====================
lt=0
rt=max(times)*n
res=0
# times.sort()
def count(mid):
    cnt=0
    for i in range(len(times)):
        cnt+=mid//times[i]
    return cnt
while lt<=rt:
    mid=(lt+rt)//2
    if count(mid)>=n:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)