import sys
n,m = map(int,sys.stdin.readline().split())
# 구명보트는 2명이하
# 한 개에 탈 수 있는 총 무게도 Mkg 이하
weight=list(map(int,input().split()))
weight.sort(reverse=True)
cnt=0
while len(weight)!=0:
    if m-weight[0]<weight[len(weight)-1]:
        del weight[0]
        cnt+=1
    else:
        del weight[0]
        if len(weight)!=0:
            weight.pop()
        cnt+=1
print(cnt)
