"""
currencies의 각 요소는 이 나라에서 사용되는 화폐의 단위를 나타낸다.
이 나라의 화폐를 이용하여, wantMoney만큼의 돈을 거슬러주는 모든 방법의 수를 리턴하시오.
"""
# 위의 풀이가 왜 안됬는지 찾기
# def solution(currencies, wantMoney):
#     # DP
#     price = [1] + [0] * wantMoney
#     for i in currencies:
#         for j in range(i, wantMoney+1):
#             if j >= i:
#                 price[j] += price[j-i]
#     print(price)
#     return price[-1]


def solution(currencies, wantMoney):
    # dp생성
    dp = [[0] * (wantMoney + 1) for _ in range(len(currencies))]
    dp[0][0] = 1

    # 첫번째 금액으로 n원을 구성 가능하면 1로 변경
    for i in range(currencies[0], wantMoney + 1, currencies[0]):
        dp[0][i] = 1

    # y: 지불가능한 동전
    for y in range(1, len(currencies)):
        # x: 거슬러줘야하는 금액
        for x in range(wantMoney + 1):
            # 거슬러줘야하는 금액을 지불가능한 동전보다 클 경우
            if x >= currencies[y]:
                dp[y][x] = (dp[y - 1][x] + dp[y][x - currencies[y]])
            # 반대의 경우
            else:
                dp[y][x] = dp[y - 1][x]

    # 마지막 값 출력
    return dp[-1][-1]

print(solution([1,5,10],10))
print(solution([4,25,40],80))
print(solution([10,11,38],90))
# print(solution([1,21,24,31,35,37,47],57))
# print(solution([10,11,38,39,40,41,48],55))