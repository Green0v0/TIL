import sys
N = int(sys.stdin.readline().rstrip())

# 데이터 추가하는 2가지 방법
got = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

# got = []
# for _ in range(N):
#     got.append(list(map(int,sys.stdin.readline().split())))

# 회전시키기
# 행, 0:왼쪽 1:오른쪽, 몇 칸
M = int(sys.stdin.readline().rstrip())

# 처음 생각한 방법이 틀림
# 회전 횟수(how)가 주어진 리스트(got)의 길이보다 길다면 오류가 발생..!
# for _ in range(M):
#     row, vec, how = map(int,sys.stdin.readline().split())
#     # index와 몇 번째의 차이
#     row = row-1
#     if vec == 0:
#         got[row] = got[row][how:] + got[row][:how]
#     else:
#         got[row] = got[row][-how:] + got[row][:-how]

# 수업 해설
for i in range(M):
    h,t,k = map(int,sys.stdin.readline().split())
    if t==0:
        for _ in range(k):
            got[h-1].append(got[h-1].pop(0))
    else:
        for _ in range(k):
            got[h-1].insert(0,got[h-1].pop())

# 영역계산에서 오류 NO, 회전하는 곳에서 틀림...왜일까..?
# 모래시계 영억 계산
total = 0
for t in range(N):
    # 반복 횟수
    if t == 0:
        i = N
    elif t <= N//2:
        i -= 2
    else:
        i += 2
    # 시작점
    j = (N//2) - (i//2)
    # print(i,j)
    for k in range(i):
        total += got[t][j]
        j+=1

# total = 0
# s = 0
# e = N-1
# for i in range(N):
#     for j in range(s,e+1):
#         total +=  got[i][j]
#     if i<N//2:
#         s+=1
#         e-=1
#     else:
#         s-=1
#         e+=1

print(total)
# 3,4번 틀림