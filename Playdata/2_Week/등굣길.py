# DP
# 오른쪽과 아래쪽으로만 움직여짐
# 최단경로의 개수를 1000000007로 나눈 나머지를 return
# m,n은 1,1이 아님 물이 잠긴 지역은 0~10, 집과 학교가 물에 잠긴 경우 x
def solution(m, n, puddles):
    board = [[True]*m for _ in range(n)]

    # 열, 행 바껴있었음 ㅡㅡㅡ
    for x, y in puddles:
        board[y-1][x-1] = 0

    for i in range(n):
        for j in range(m):
            # 0은 False취급
            if board[i][j] != True:
                continue

            if i == 0 and j == 0:
                board[i][j] = 1
                continue

            # check를 회전하며 좌표확인
            if i - 1 < 0:
                cx = 0
                cy = board[i][j-1]

            elif j - 1 < 0:
                cx = board[i-1][j]
                cy = 0
            else:
                cx = board[i-1][j]
                cy = board[i][j-1]
            v = cx + cy
            board[i][j] = v

    # print(board[-1][-1])
    print(board)

print(solution(4,3,[[2,2]]))
print(solution(4,4,[[3,1],[2,3]]))

# 다른 사람 풀이
def solution1(m,n,puddles):
    grid = [[0]*(m+1) for i in range(n+1)] #왼쪽, 위로 한줄씩 만들어서 IndexError 방지
    if puddles != [[]]:                    #물이 잠긴 지역이 0일 수 있음
        for a, b in puddles:
            grid[b][a] = -1                #미리 -1로 체크
    grid[1][1] = 1
    for j in range(1,n+1):
        for k in range(1,m+1):
            if j == k == 1:                #(1,1)은 1로 만들어두고, 0이 되지 않도록
                continue
            if grid[j][k] == -1:           #웅덩이는 0으로 만들어 다음 덧셈 때 영향끼치지 않게
                grid[j][k] = 0
                continue
            grid[j][k] = (grid[j][k-1] + grid[j-1][k])%1000000007   #[a,b] = [a-1,b] + [a,b-1] 공식

    return grid[n][m]

def solution2(m, n, puddles):
    info = dict([((2, 1), 1), ((1, 2), 1)])
    for puddle in puddles:
        info[tuple(puddle)] = 0

    def func(m, n):
        if m < 1 or n < 1:
            return 0
        if (m, n) in info:
            return info[(m, n)]
        return info.setdefault((m, n), func(m - 1, n) + func(m, n - 1))
    return  func(m, n) % 1000000007