# 야근지수
# from queue import PriorityQueue
import heapq
def solution(n,works):
    heap = []

    for i in works:
        heapq.heappush(heap,-i)

    for n in range(n):
        value = heapq.heappop(heap)
        if value == 0:
            value = 0
        else:
            value += 1
        heapq.heappush(heap,value)

    result = sum(map(lambda x:x**2, heap))
    return result

# 다시 풀어봄
import heapq
def resolution(n, works):
    if sum(works) <= n:
        return 0

    heap = []
    for value in works:
        heapq.heappush(heap, -value)

    for _ in range(n):
        pop = heapq.heappop(heap)
        heapq.heappush(heap, pop + 1)

    return sum([x**2 for x in heap])

solution([4,3,3],4)
print(solution(4,[4,3,3]))
print(solution(3,[1,1]))