# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int,input().split())
    answer = ''
    board = []
    def calculation(board):
        global answer
        for b in range(len(board)):
            for i in range(0, len(board[0]) - m + 1):
                target = board[b][i : i + m]
                if target == target[::-1]:
                    answer = target
                    break
    for _ in range(n):
        board.append(list(input()))

    new_board = list(zip(*board))
    calculation(board)
    calculation(new_board)
    print(f'#{test_case} {"".join(answer)}')

