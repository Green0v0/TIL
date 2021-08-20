import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    cnt = 0
    board = []
    def calculation(board):
        global cnt
        for b in range(len(board)):
            for j in range(len(board[0])):
                for i in range(len(board[0]), 0, -1):
                    target = board[b][j : i + 1]
                    if i < cnt:
                        break
                    if target == target[::-1]:
                        cnt = max(cnt, len(target))
                        break

    for _ in range(100):
        board.append(list(input()))
    new_board = list(zip(*board))

    calculation(board)
    calculation(new_board)
    print(f'#{n} {cnt}')