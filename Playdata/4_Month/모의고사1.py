def solution(apparentGanin):
# 몸무게의 제곱을 보여주는 체중계
# apparentGain (제인 현재 몸무게의 제곱과 예전 몸무게의 제곱의 차이)
# 가장 최근의 측정 이후 가능한 제인의 실제 몸무게를 오름차순으로 정렬한 정수값의 배열을 리턴하시오.
#     n = (apparentGanin + 1) // 2
#     result = []
#     for i in range(1, n + 1):
#         for j in range(1,i + 1):
#             if i**2 - j**2 == apparentGanin:
#                 result.append(i)
#     return result

# 투포인터
    n = (apparentGanin + 1) // 2
    weight = list(range(1,n+1))
    result = []
    # idx
    l, r = 0, 1
    while r < n:
        curr = weight[r]**2 - weight[l]**2
        if r <= l:
            break
        if curr < apparentGanin:
            r += 1
        elif curr > apparentGanin:
            l += 1
        elif curr == apparentGanin:
            result.append(weight[r])
            l += 1

    return result

# print(solution(233))
# print(solution(15))
# print(solution(5))
print(solution(1440))
