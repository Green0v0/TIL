# 자동차로 이동 가능한 전체 가능한 경로 수를 출력하는 프로그램을 작성하라.
# 20170805로 나눈 나머지 값을 출력
# 0 제약없음, 1 통행금지, 2 과거모션 그대로
# def solution(m,n,city_map):
#     # poss는 가능한 경우의 수를 체크
#     # dp는 점화식이다.
#     # 2일때는 과거 점수 그대로 가져오기 그런데 범위를 조정해줘야한다.
#     poss = [[0] * n for _ in range(m)]
#     for i in range(m):
#         for j in range(n):
#             if (i == 0 or j == 0) and city_map[i][j] != 1:
#                 poss[i][j] = 1
#                 continue
#             x = poss[i - 1][j]
#             y = poss[i][j - 1]
#             if city_map[i][j-1] == 1 or city_map[i-1][j] == 1:
#                 poss[i][j] = x if poss[i][j-1] == 1 else y
#             if city_map[i][j-1] == 2:
#                 verti = [k for k in zip(*poss)]
#                 for ny in range(j,-1,-1):
#                     if verti[i][ny] != 2:
#                         y = poss[i][ny]
#                     else:
#                         y = 0
#             elif city_map[i-1][j] == 2:
#                 for nx in range(i,-1,-1):
#                     if city_map[nx][j] != 2:
#                         x = poss[nx][j]
#                     else:
#                         x = 0
#             poss[i][j] = x + y
#             print(x,y)

# 1) 왼쪽 -> 오른쪽 + 2) 위쪽 -> 아래쪽
# 다이나믹 프로그래밍
# 각 방향의 경우의 수를 구하는 문제로 나눌 수 있음
# 메모이제이션 : 이미 계산한 결과 배열에 저장
def solution(m,n,city_map):
    mod = 20170805
    goRight = [[0] * (n+1) for _ in range(m+1)]
    goDown = [[0] * (n+1) for _ in range(m+1)]
    goRight[1][1] = 1
    goDown[1][1] = 1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if city_map[i-1][j-1] == 0:
                goRight[i][j] += (goRight[i-1][j] + goDown[i][j-1]) % mod
                goDown[i][j] += (goRight[i-1][j] + goDown[i][j-1]) % mod
            elif city_map[i-1][j-1] == 1:
                goRight[i][j] = 0
                goDown[i][j] = 0
            else:
                goRight[i][j] = goRight[i-1][j]
                goDown[i][j] = goDown[i][j-1]

    return (goRight[m-1][n] + goDown[m][n-1]) % mod

print(solution(3,3,[[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(solution(3,6,[[0, 2, 0, 0, 0, 2], [0, 0, 2, 0, 1, 0], [1, 0, 0, 2, 2, 0]]))