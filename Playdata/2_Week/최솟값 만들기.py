import heapq
def solution(A,B):
    heapq.heapify(A)
    # 최대힙
    maxheap = []
    for i in B:
        heapq.heappush(maxheap,-i)

    total = 0
    for j in range(len(A)):
        total += (heapq.heappop(A)*(-heapq.heappop(maxheap)))
    # print(total)
    return total

# return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))

solution([1,4,2],[5,4,4])