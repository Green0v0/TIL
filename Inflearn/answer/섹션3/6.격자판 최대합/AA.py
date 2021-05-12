import sys
N = int(sys.stdin.readline().rstrip())
li = []
for i in range(N):
    li.append(list(map(int,sys.stdin.readline().split())))
# print(li)
def row(x):
    sum_r = 0
    for j in range(N):
        if sum_r < sum(li[j]):
            sum_r = sum(li[j])
    return sum_r
def col(x):
    sum_c = 0
    for j in range(N):
        total = 0
        for k in range(N):
            total = total + li[k][j]
        if sum_c < total:
            sum_c = total
    return sum_c
def diag(x):
    total = 0
    for i in range(N):
        total = total + li[i][i]
    total2 = 0
    for i in range(N):
        total2 = total2 + li[i][N-i-1]
    if total > total2:
        return total
    else:
        return total2
final = row(li)
if final < col(li):
    final = col(li)
if final < diag(li):
    final = diag(li)

print(final)
