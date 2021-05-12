import sys
N = int(sys.stdin.readline().rstrip())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
cnt = 0
# point_n,point_s,point_w,point_e = 0
for i in range(N):
    for j in range(N):
        try:
            point_n = a[i-1][j]
            point_s = a[i+1][j]
            point_w = a[i][j-1]
            point_e = a[i][j+1]
            if i - 1 == -1:
                point_n = 0
            if j - 1 == -1:
                point_w = 0
        except:
            if i + 1 == N:
                point_n = a[i - 1][j]
                point_w = a[i][j - 1]
                point_s = 0
                if j + 1 == N:
                    point_e = 0
                else:
                    point_e = a[i][j + 1]
            if j + 1 == N:
                point_e = 0
        # 이거를 어떻게 처리해야할까..?
        # print(f'i = {i}, j = {j} , n = {point_n}, s = {point_s}, w = {point_w}, e = {point_e}')
        if a[i][j] > point_n and a[i][j] > point_s and a[i][j] > point_w and a[i][j] > point_e:
            cnt+=1
            # print(i,j)
print(cnt)