# import sys
# N = int(sys.stdin.readline().rstrip())
#
# # n = N/3
# def pattern(N):
#     po = N//3
#     n = 1
#     for i in range(1, 9):
#         if N == 3**i:
#             n = i
#     # print(n) : 2
#     # print(po) : 3
#     for i in range(N):
#         for j in range(N):
#             if (po <= i and i < 2*po) and (po <= j and j < 2*po):
#                 print(' ',end='')
#             else:
#                 print('*',end='')
#         print()

# pattern(N)

# 못품 ㅠㅠㅠ

# 풀이 1
# 프랙탈 도형을 그리는 문제이다. 프랙탈 같은 경우는 최소 단위로 쪼갤 수 있기에 분할 정복 알고리즘 (Divide and Conquer)을
# 이용해 풀 수 있다. 분할 정복 알고리즘의 단계를 분할, 정복, 합치기 세 개로 나누면 쉽게 기억할 수 있다.
def stars(n):
    matrix = []
    for i in range(3*len(n)):
        if i // len(n) == 1:
            matrix.append(n[i%len(n)]+" "*len(n)+n[i%len(n)])
        else:
            matrix.append(n[i%len(n)]*3)
    return(list(matrix))
star = ["***","* *","***"]
# star = ["*"]
n = int(input())
k = 0
# k = 1
while n!=3:
    n = int(n/3)
    k+=1
for i in range(k):
    star = stars(star)
for i in star:
    print(i)

# 풀이 2
# "*"로 다 채워놓은 다음, 빈 칸을 찾아 없애는 방식
n=int(input()) # input
arr = [["*"]*n for _ in range(n)] # output array 생성
v=n;cnt=0
while v!=1: # 입력받은 n이 3의 몇승?
    v/=3
    cnt+=1
for cnt_ in range(cnt):
    idx = [i for i in range(n) if (i // 3 ** cnt_) % 3 == 1]
    # 빈칸으로 채울 행/열 index
    for i in idx:
        for j in idx:
            arr[i][j] = " "
# 출력
print('\n'.join([''.join([str(i) for i in row]) for row in arr]))

# 위 코드 funcion으로 묶기
def star(i):
    global arr # arr 전역변수화; r에서 "<<-" 와 같은 기능
    idx = [i for i in range(n) if (i // 3 ** cnt_) % 3 == 1]
    for i in idx:
        for j in idx:
            arr[i][j] = " "
n=int(input())
v=n;cnt=0
while v!=1:
    v/=3
    cnt+=1

arr = [["*"]*n for _ in range(n)]

for cnt_ in range(cnt):
    star(cnt_)
print('\n'.join([''.join([str(i) for i in row]) for row in arr]))

# 풀이 3
import sys

num = int(input())

def star(i, j):
    while(i != 0):
        # 몫이 1인 경우
        if(i % 3 == 1 and j % 3 == 1):
            sys.stdout.write(' ')
            return None
        # 3으로 나누어서 위의 if문에 걸리면 그 부분도 빈칸 처리
        i = i // 3
        j = j // 3
    sys.stdout.write('*')

for i in range(num):
    for j in range(num):
            star(i, j)
    sys.stdout.write('\n')