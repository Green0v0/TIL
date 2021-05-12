from collections import deque
# 왜 DFS로 생각했지? 최단거리를 구하는 것이므로 BFS!
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int,list(input()))))

q = deque([[0,0]])
cnt = 0
while q:
    x, y = q.popleft()
    if x == 0 and y == 0:
        board[x][y] = -1 # 첫 출발지 2로 만들어서 visited 표현
    for i, j in [(1,0),(0,1),(-1,0),(0,-1)]:
        nx, ny = x + i, y + j
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if board[nx][ny] == 1:
            q.append([nx, ny])
            board[nx][ny] = board[x][y] - 1
        nx, ny = x, y

# print(board)
print(abs(board[n-1][m-1]))

# https://pacific-ocean.tistory.com/265
# https://j-remind.tistory.com/52
# https://velog.io/@jengyoung/baekjoon2178
# https://chancoding.tistory.com/64
# https://hjp845.tistory.com/94

# 다른 사람 풀이
from sys import stdin
N, M = map(int, stdin.readline().split())
# matrix 배열
matrix = [stdin.readline().rstrip() for _ in range(N)]
# 방문경로 배열
visited = [[0]*M for _ in range(N)]
# 좌/우/위/아래 방향 이동
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# BFS 경로 탐색
# queue 방식 사용
queue = [(0,0)]
visited[0][0] = 1

while queue:
    x, y = queue.pop(0)

    if x == N-1 and y == M-1:
        # 최종 경로 도착
        print(visited[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))

# notion
import sys
from collections import deque
N, M = map(int, input().split())
maze = [input() for i in range(N)]
maze = list(map(lambda x: list(x), maze))

dist = [[-1] * M for i in range(N)] # 방문여부 확인하기 위해 -1로 초기화

# 상하좌우
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
q.append((0,0))
dist[0][0] = 0 # 방문표시를 해줌과 동시에 초기 출발지를 정해주는 작업
cnt = 0
while q:
    cur = q.popleft()
    for i in range(4):
        nx = cur[0] + dx[i]
        ny = cur[1] + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if dist[nx][ny] < 0 and maze[nx][ny] == 1:
                dist[nx][ny] = dist[cur[0]][cur[1]] + 1
                q.append((nx, ny))

cnt = dist[N-1][M-1] + 1
print(cnt)
