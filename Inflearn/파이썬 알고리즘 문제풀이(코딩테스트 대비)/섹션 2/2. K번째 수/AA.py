# 오름차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성
import sys
T = int(sys.stdin.readline().rstrip())
# N개의 숫자 s번째부터 e번째 까지의 수를 오름차순 k번째 숫자 출력
for i in range(T):
    N, s, e, k = map(int,sys.stdin.readline().split())
    li = list(map(int,sys.stdin.readline().split()))
    li = li[s-1:e]
    li = sorted(li)
    print(f'#{i+1} {li[k-1]}')