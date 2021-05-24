"""
실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때,
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.
"""
from collections import Counter
def solution(N, stages):
    result = [0.0] * N
    stage = Counter(stages) # Counter({2: 3, 3: 2, 1: 1, 6: 1, 4: 1})
    challenger = len(stages) # 전체 도전자
    for i in range(1, len(result) + 1):
        if challenger == 0:
            result[i-1] = (i, 0)
            continue
        result[i-1] = (i, stage[i]/challenger)
        challenger -= stage[i]

    result.sort(key=lambda x:(-x[1], x[0]))
    answer = list(map(list,zip(*result)))

    return answer[0]
    # print(result)

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))
print(solution(5,[1,2,2,1,3])) #result : [3,2,1,4,5]

# 다른 사람 풀이 : 딕셔너리 활용
def solution(N, stages):
    result = {}
    denominator = len(stages)

    for stage in range(1, N + 1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0

    return sorted(result, key=lambda x: result[x], reverse=True)