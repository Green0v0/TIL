n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
new = []
for i in range(0, n-7):
    for j in range(0, m-7):
        new.append((i,j))
result = float('inf')
for c in ('B','W'):
    for start in new:
        cx, cy = start
        check = c
        new_s = cx + cy
        cnt1 = 0

        for x in range(cx,cx+8):
            for y in range(cy, cy+8):
                if (new_s - (x+y)) % 2 == 0 and board[x][y] == check:
                    continue
                elif (new_s - (x+y)) % 2 != 0 and board[x][y] != check:
                    continue
                cnt1 += 1
        result = min(result,cnt1)

print(result)

# 첫번째 풀이
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
new = []
for i in range(0, n-7):
    for j in range(0, m-7):
        new.append((i,j))
# print(new)
result1 = float('inf')
result2 = float('inf')
for start in new:
    cx, cy = start
    check = 'B'
    new_s = cx + cy
    cnt1 = 0

    for x in range(cx,cx+8):
        for y in range(cy, cy+8):
            if (new_s - (x+y)) % 2 == 0 and board[x][y] == check:
                continue
            elif (new_s - (x+y)) % 2 != 0 and board[x][y] != check:
                continue
            cnt1 += 1
    result1 = min(result1,cnt1)

    check = 'W'
    cnt2 = 0

    for x in range(cx, cx + 8):
        for y in range(cy, cy + 8):
            if (new_s - (x + y)) % 2 == 0 and board[x][y] == check:
                continue
            elif (new_s - (x + y)) % 2 != 0 and board[x][y] != check:
                continue
            cnt2 += 1
    result2 = min(result2, cnt2)


print(min(result1, result2))