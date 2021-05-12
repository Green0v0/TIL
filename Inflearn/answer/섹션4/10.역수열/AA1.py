import sys
n = int(input())
su=list(map(int,sys.stdin.readline().split()))
empty=[n+1]*(n)
for i in range(8):
    # 1은 1보다 큰 수가 없으니 미리 지정
    if i == 0:
        empty[su[0]] = i+1
        continue
    cnt=0 #앞의 자신보다 큰수
    ncnt=0 #앞의 자신보다 작은수
    j=0 #empty의 인덱스
    while cnt<su[i]:
        if empty[j]>i+1:
            j+=1
            cnt+=1
        else:
            ncnt+=1
            j+=1
            cnt+=0
    while empty[cnt+ncnt] != n+1:
        ncnt+=1
    empty[cnt+ncnt]=(i+1)
print(empty)