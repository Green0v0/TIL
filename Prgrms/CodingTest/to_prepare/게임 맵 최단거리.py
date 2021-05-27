# bfs
# x, y 좌표 확인 잘하기.
from collections import deque
def solution(maps):
    visited = [[True] * len(maps[0]) for _ in range(len(maps))]
    n, m = len(maps[0]), len(maps)
    dq = deque([[0,0]])
    # visited[0][0] = False
    for i in maps:
        print(i)
    while dq:
        cx, cy = dq.popleft()
        for x, y in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = cx + x, cy + y
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if visited[nx][ny] == False:
                continue
            if maps[nx][ny] == 0:
                continue
            dq.append([nx,ny])
            visited[nx][ny] = False
            maps[nx][ny] = maps[cx][cy] + 1
            if nx == m - 1 and ny == n - 1:
                print(maps)
                return maps[m-1][n-1]
    # return maps[-1][-1] if visited[-1][-1] == False else -1
    return -1

# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1],[1,0,1],[1,0,1],[1,1,1]]))
# print(solution([[1,0],[1,1]]))
# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))