def solution(prices):
    prices = list(set(prices))
    if len(prices) < 3:
        return -1
    prices.sort()
    return prices[2]

print(solution([10,10,10,20,20,20,30,30,40,40]))
print(solution([80,80,90,90]))