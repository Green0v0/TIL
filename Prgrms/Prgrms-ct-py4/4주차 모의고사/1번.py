# 땅따먹기
def solution(land):
    for l in range(1, len(land)):
        for i in range(4):
            land[l][i] = max(land[l-1][:i] + land[l-1][i+1:]) + land[l][i]

    return max(land[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))