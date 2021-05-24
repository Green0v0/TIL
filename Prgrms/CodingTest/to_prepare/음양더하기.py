def solution(absolutes, signs):
    answer = 0
    for idx, value in enumerate(absolutes):
        answer += value if signs[idx] else -value
    return answer

print(solution([4,7,12],[True,False,True]))