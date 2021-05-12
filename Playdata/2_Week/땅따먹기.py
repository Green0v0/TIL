# 같은 열을 연속해서 밟으면 안된다!
# idx = 0
# index 맨앞에꺼..
# 5234
# 2221
# {6}662
# {8}765

# DP
def solution(land):
    for i in range(0, len(land)-1):
        land[i+1][0] += max(land[i][1],land[i][2],land[i][3])
        land[i+1][1] += max(land[i][0],land[i][2],land[i][3])
        land[i+1][2] += max(land[i][0],land[i][1],land[i][3])
        land[i+1][3] += max(land[i][0],land[i][1],land[i][2])
    return max(land[len(land)-1])

# 비슷한 다른 풀이
def solution1(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
print(solution([[1,2,3,4],[1,2,6,8],[4,3,2,1]]))
print(solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]])) #20