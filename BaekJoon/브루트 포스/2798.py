import sys
N, M = map(int,sys.stdin.readline().split())
list_N = list(map(int,sys.stdin.readline().split()))
sum_list = []
for i in list_N:
    for j in list_N:
        for k in list_N:
            if i+j+k <= M and i!=j and i!=k and j!=k:
                sum_list.append(i+j+k)
# sum_set = set(sum_list)
# print(len(sum_set))
# print(sum_set)
print(max(sum_list))

# 다른 풀이 1
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = len(a)
sum = 0
for i in range(0, b - 2):
        for j in range(i + 1, b - 1):
                for k in range(j + 1, b):
                        if a[i] + a[j] + a[k] > m:
                                continue
                        else:
                                sum = max(sum, a[i] + a[j] + a[k])
print(sum)
