import sys
star = '*'
N = int(sys.stdin.readline().rstrip())
for idx in range(N):
    if (idx+1) < N :
        print(star*(idx+1))
    else :
        for i in range(N) :
            print(star*(N - i))

# 다른 방법
case = int(input())
for i in range(1,case):
    print('*'*i)
for i in range(case,0,-1):
    print('*'*i)

# 다른 방법 2
# '{0:^10d}{1:^10f}{2:^10s}'.format(n,f,s) #최소 필드 길이가 10이고 가운데 정렬