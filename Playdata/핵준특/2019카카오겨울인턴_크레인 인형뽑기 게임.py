# 터트려져 사라진 인형의 개수를 return
# board의 숫자는 인형 종류 moves의 숫자는 이동하는 곳
def solution(board, moves):
    stack = []
    result = 0
    for m in moves:
        # m은 크레인 위치
        nm = m - 1
        # 0이면 다음 줄로 감! 아니면 0으로 바꾸고 stack에 추가
        for line in board:
            if line[nm] == 0:
                continue
            else:
                new = line[nm]
                line[nm] = 0
                if len(stack) == 0:
                    stack.append(new)
                elif stack[-1] != new:
                    stack.append(new)
                elif stack[-1] == new:
                    result += 1
                    stack.pop()
                break

    return result*2

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))

# 다른 사람 풀이
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break

    return answer

# 다른 사람 풀이 2
def solution(board, moves):
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    a, s = 0, [0]

    for m in moves:
        if len(cols[m - 1]) > 0:
            if (d := cols[m - 1].pop(0)) == (l := s.pop()):
                a += 2
            else:
                s.extend([l, d])

    return a

# notion
from collections import deque

def solution(board, moves):
    moves = deque(moves)
    buckets = []
    cnt = 0

    while moves:
        move = moves.popleft()

        for i in range(len(board)):
            doll = board[i][move - 1]

            if doll != 0:
                board[i][move - 1] = 0

                if buckets and buckets[-1] == doll:
                    buckets.pop()
                    cnt += 2
                else:
                    buckets.append(doll)
                break

    return cnt
