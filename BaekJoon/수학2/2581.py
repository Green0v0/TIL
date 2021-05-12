import sys
M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
def sosu(M,N):
    result = []
    total = 0
    for i in range(M,N+1):
        cnt = 0
        if i == 1:
            continue
        for j in range(1,i+1):
            if i%j == 0:
               cnt+=1
               if cnt > 2:  # 2보다 크면 소수가 아니므로(소수는 1과 자기자신으로만 나뉨) 바로 다음식 진행
                   break
                # 3024ms에서 608ms로 줄였다 / 코드 길이가 문제가 아닌 함수의 문제일 수 있음.
        # print(f'{i}값의 cnt : {cnt}')
        if cnt == 2:
            total += i
            result.append(i)
    if len(result) == 0:
        print(-1)
    else:
        print(total)
        print(result[0])

sosu(M,N)
# if len(sosu(M,N)) == 0:
#     print(-1)
# else:
#     total = 0
#     for i in sosu(M,N):
#         total += i
#     print(total)
#     print(sosu(M,N)[0])