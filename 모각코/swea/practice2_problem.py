# H: 집, ABC: 기지국 123
tk = int(input())
n = int(input())
board = []
def gizi(alpha):
    # answer = []
    # for n in range(2):
    #     for i in range(1, 4):
    #         for cx in range(2):
    #             l = [0, 0]
    #             if n == 0:
    #                 l[cx] = l[cx] + i
    #             else:
    #                 l[cx] = l[cx] - i
    #             answer.append(l)
    if alpha == 'A':
        return [[0, 1], [1, 0], [-1, 0], [0, -1]]
    elif alpha == 'B':
        return [[1, 0], [0, 1], [2, 0], [0, 2], [-1, 0], [0, -1], [-2, 0], [0, -2]]
    else:
        return [[1, 0], [0, 1], [2, 0], [0, 2], [3, 0], [0, 3], [-1, 0], [0, -1], [-2, 0], [0, -2], [-3, 0], [0, -3]]

for _ in range(n):
    b = list(input())
    board.append(b)

for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] == 'X' or board[i][j] == 'H':
            continue
        line = gizi(board[i][j])
        for x, y in line:
            cx, cy = i + x, j + y
            if cx < 0 or cx >= n or cy < 0 or cy >= n: # 거리계산
                continue
            if board[i+x][j+y] != 'H': # 주변에 기지국은 제외외
               continue
            board[i+x][j+y] = 'X'

cnt = 0
for o in range(len(board)):
    for p in range(len(board)):
        if board[o][p] == 'H':
            cnt += 1
print(cnt)