import sys

T = int(sys.stdin.readline().rstrip())
N = list(map(int,sys.stdin.readline().split()))

# 런타임 에러
# def bubble_swap(x,i,j):
#     x[i], x[j] = x[j], x[i]
#
# def bubblesort(x):
#     for size in reversed(range(len(x))):
#         for i in range(size):
#             if x[i] > x[i+1]:
#                 bubble_swap(x,i,i+1)
#
# bubblesort(N)
# print(f'{N[0]} {N[len(N)-1]}')

# 다시 풀기
temp1 = N[0]
temp2 = N[0]
for idx in range(1,len(N)):
    if temp1 > N[idx]:
        temp1 = N[idx]
    # else :
    #     temp = temp

    if temp2 < N[idx]:
        temp2 = N[idx]

print(f'{temp1} {temp2}')

# 다른 풀이
Case = int(input())
num_list = list(map(int, input().split()))
print('{} {}'.format(min(num_list), max(num_list)))

# 다른 풀이 2
a = int(input())
b = list(map(int, input().split()))
b.sort()
print(b[0])
print(b[a-1])