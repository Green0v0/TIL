import sys
sys.stdin = open("./input/input_1.txt", "r")

T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    board = []
    result = 0
    for _ in range(n):
        board.append(list(map(int,input().split())))
    for i in range(n):
        for j in range(n):
            pari = 0
            for x in range(i, i + m):
                if x >= n:
                    continue
                for y in range(j, j + m):
                    if y >= n:
                        continue
                    pari += board[y][x]
            result = max(result, pari)
    print(f'#{t + 1} {result}')