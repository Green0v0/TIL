import sys
matrix = [list(map(int,sys.stdin.readline().split())) for i in range(7)]
x = [5,0,-5,0]
y = [0,5,0,-5]
x_3 = [3,0,-3,0]
y_3 = [0,3,0,-3]
# 좌표를 다 나눠놔야하는 건가?
for i in range(7):
    for j in range(7):
        if matrix[i][j] == matrix[i+x[i]][j+y[j]]:
            continue
        pass