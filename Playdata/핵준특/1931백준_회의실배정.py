# 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.
import sys
N = int(sys.stdin.readline())
schedule = []
for _ in range(N):
    s, e = map(int, input().split())
    schedule.append((s,e))

# greedy는 정렬이지!
schedule.sort(key = lambda x:(x[1],x[0]))
# [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
start = 0
end = 1
cnt = 0
for i, j in schedule:
    if i >= start:
        start = end
        cnt += 1
    # print(f'start = {start}, end = {end}, cnt = {cnt}')
print(cnt)

# notion
# 여러 경우 중 하나를 선택할 때 가장 좋다고 생각하는 것을 선택해 나가면 결과적으로도 최선.
import sys

N = int(sys.stdin.readline())
meetings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 끝나는 시간 기준으로 정렬
def solution(N, meetings):
    meetings.sort(key = lambda x: (x[1], x[0]))

    cnt = 0
    end_time = 0
    for meeting in meetings:
        if meeting[0] >= end_time:
            end_time = meeting[1]
            cnt += 1

    return cnt