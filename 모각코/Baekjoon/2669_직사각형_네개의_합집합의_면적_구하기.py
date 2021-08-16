rectangle = []
mx, my = 0, 0
for _ in range(4):
    x1, y1, x2, y2 = map(int,input().split())
    if mx < x2:
        mx = x2
    if my < y2:
        my = y2
    rectangle.append([x1, y1, x2, y2])

board = [[0 for _ in range(mx + 1)] for _ in range(my + 1)]
for x1, y1, x2, y2 in rectangle:
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            board[y][x] = 1
            # 1줄이 2줄 취급됨 다시 구현

for b in board:
    print(b)