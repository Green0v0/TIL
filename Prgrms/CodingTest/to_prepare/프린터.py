from collections import deque


def solution(priorities, location):

    priorities = deque(priorities)
    cnt = 0
    while priorities:
        J = priorities.popleft()
        if not priorities:
            return cnt+1
        max_other = max(priorities)
        if J < max_other:
            priorities.append(J)
        else:
            cnt += 1
            if location == 0:
                break
        location -= 1
        if location < 0:
            location = len(priorities) - 1

    return cnt

print(solution([2, 1, 3, 2],1))
print(solution([1, 1, 9, 1, 1, 1],0))
print(solution([9],0))

# 다른 사람 풀이
def solution1(priorities, location):
    queue = [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer