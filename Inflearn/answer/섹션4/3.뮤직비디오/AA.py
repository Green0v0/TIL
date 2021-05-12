import sys
n,m = map(int,sys.stdin.readline().split())
line=list(map(int,input().split())); res=0
# 이해 후 수정하기
# 9 9
# 1 2 3 4 5 6 7 8 9
def Count(len):
    len_1=len
    len_2=len
    cnt=0
    for x in line:
        if len_2<=x:
            cnt+=1
            len_2=len_1
        len_2 -= x
    return cnt
lt=1
rt=sum(line)
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=m:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)