import sys

N, X = map(int, sys.stdin.readline().split())
# print(N, X)
# print(type(N), type(X))

# 수열은 N개 주어진다.

A = list(map(int,sys.stdin.readline().split()))
# print(type(A[0]))


li = []
for idx in range(N):
    if A[idx] < X :
        # li.append(A[idx])
        print(A[idx], end=' ')
    else :
        pass
