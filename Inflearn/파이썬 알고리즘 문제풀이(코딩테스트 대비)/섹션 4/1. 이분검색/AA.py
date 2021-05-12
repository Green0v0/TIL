# 이분탐색(결정 알고리즘)
import sys
N, M = map(int, sys.stdin.readline().split())
li = list(map(int,sys.stdin.readline().split()))
li.sort()
lt = 0
rt = N-1
while lt<=rt:
    mid = (lt+rt)//2
    if li[mid] == M:
        print(mid+1)
        break
    elif li[mid]>M:
        rt = mid-1
    else:
        lt = mid+1
