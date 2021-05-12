# 15:20 ~15:50
# 50달러 이상 지출시 10달러 할인 -> 합계산시 따로 지불보다 적게 지불 가능
# 세 자매가 모든 상품을 구입하는데 드는 최소 비용을 return
# idea : Greedy
import heapq
def solution(goods):
    heapq.heapify(goods)
    check = 0
    result = 0

    for _ in range(len(goods)):
        check += heapq.heappop(goods)
        if check > 50:
            result += (check - 10)
            check = 0

    return result

print(solution([46,62,1]))