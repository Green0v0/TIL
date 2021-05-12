# 완전탐색으로 3개를 고른 후 BFS로 모두 퍼지고 0인 부분 count하여 max를 확인
import sys
import copy
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
board = []
for i in range(M):
    board.append(list(map(int,sys.stdin.readline().split())))
# 완전 탐색으로 3개 골라 벽 세우기
zero = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            zero.append((i,j))
# print(zero)
# 3개를 골랐음
co = combinations(zero,3)
# 벽을 세우기 -> 1을 추가 & 함수로 BFS 그렇다면 함수 BFS 구현
# print(co)
# BFS 구현 함수
def bfs(board): # 1이 추가된 board가 들어왔을 때 bfs 0이면 확장
    pass

# count하여 max값을 구하는 for문

