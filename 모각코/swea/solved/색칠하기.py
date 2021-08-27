import sys
sys.stdin = open("../input/input_3.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    board = [[0 for _ in range(30)] for _ in range(30)]
    for n in range(N):
        sx, sy, ex, ey, idx = map(int, input().split())
        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                if board[y][x] != idx:
                    board[y][x] += idx
                elif board[y][x] == 3:
                    continue
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 3:
                cnt += 1

    print(f'#{t} {cnt}')