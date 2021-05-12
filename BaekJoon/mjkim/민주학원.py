import math
n=int(input()) # input
arr = [[0]*n for _ in range(n)] # output array 생성
ex = 1
k = [ex]
# [1,3,5,3,1]
for idx in range(n-1):
    if len(k) > n//2:
        ex-=2
        k.append(ex)
    elif len(k) <= n//2:
        ex += 2
        k.append(ex)
an = 1
for i in range(n):
    abs_n = abs(i-(n//2))
    for j in range(k[i]):
        arr[i][abs_n+j] = an
        an += 1
# print(arr)
for i in arr:
    print(i)