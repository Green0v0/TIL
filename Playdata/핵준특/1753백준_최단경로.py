# from collections import deque
# import sys
# V, E = map(int, sys.stdin.readline().split())
# K = int(sys.stdin.readline()) # 시작번호
# # (u,v,w) u->v 가중치w
# # 다익스트라 알고리즘
# # 방문 리스트
# visited = [False] * (V+1)
# # 거리 계산 리스트 : 최대값으로 초기화 float('inf')도 가능
# length = [float('inf')] * (V+1)
# length[K] = 0
# # 주어진 board
# board = [list(map(int, input().split())) for _ in range(E)]
#
# d = deque([K])
# while d:
#     now = d.popleft()
#     visited[now] = True
#     # u에서 v로 가는 가중치 w : 방향이 있다.
#     for u, v, e in board:
#         if now == u and visited[v] == False:
#             d.append(v)
#             visited[v] = True
#             length[v] = min(length[v], length[now] + e)
#         # elif now == v and visited[u] == False:
#         #     d.append(u)
#         #     visited[u] = True
#         #     length[u] = min(length[u], length[now] + e)
#
# for i in range(1, len(length)):
#     print(length[i])

# notion
# 다익스트라는 heap 사용 (우선순위큐 heapq)
# heap (가중치, 목적지 노드) : 최소힙(최대힙)을 사용하는 것, 큐를 사용하는 것이 아님!!! 가장 작은 값부터 읽어냄 << 최단 거리 니까
# visited를 안쓰고, 거리 계산만 함
# 1. 현재 가중치가 제일 작은 노드를 꺼낸다
# 1-1) 현재 테이블과 비교해 가중치가 더 크면 무시한다. 더 작으면 테이블을 갱신
# 2. 현재 위치와 인접한 노드까지의 거리를 계산한다 ( = 현재 노드까지의 거리 + 현재 노드에서 특정 노드까지) & 업데이트
# 3. 힙에 원소가 없을 때까지 반복
import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
K = int(input())

distance = [INF] * (V + 1)
graph = [[] for _ in range(V + 1)]
pq = []

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

def solution(start):
    distance[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        weight, current = heapq.heappop(pq)
        if distance[current] < weight:
            continue

        for w, nextNode in graph[current]:
            if distance[nextNode] > weight + w:
                distance[nextNode] = weight + w # 갱신
                heapq.heappush(pq, (weight + w, nextNode))

solution(K)
for i in range(1, V+1):
    print("INF" if distance[i] == INF else distance[i])
