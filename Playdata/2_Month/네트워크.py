from collections import deque

def bfs(i, n, computers, visited):
    queue = deque([i])
    while queue:
        i = queue.popleft()
        visited[i] = True

        for x in range(n):
            if x == i:
                continue

            if visited[x] == True:
                continue

            if computers[i][x] == 1:
            # if computers[i][x] == 1 or computers[x][i] == 1:
                queue.append(x)

    return 1

def solution(n, computers):
    visited = [False] * n
    answer = 0

    for i in range(n):
        if not visited[i]:
            answer += bfs(i, n, computers, visited)

    return answer

# print(solution(3, [[1, 1, 0], [0, 1, 0], [0, 0, 1]]))
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(4,[[1,0,0,1],[0,1,1,0],[0,1,1,0],[1,0,0,1]])) #기대답안 : 2 , 제출답안 : 3
print(solution(5,[[1,0,0,1,0],[0,1,1,0,0],[0,1,1,0,0],[1,0,0,1,0],[0,0,0,0,1]])) # 기대답안 : 3 , 제출답안 : 4

# 다른 사람 풀이
def othersolution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer