import sys
n,m = map(int,sys.stdin.readline().split())
line=list(map(int,input().split())); res=0; largest=0
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
# for i in range(n):
#     tmp = int(input())
#     line.append(tmp)
#     largest=max(largest,tmp)
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