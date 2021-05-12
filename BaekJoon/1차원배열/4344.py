import sys

C = int(sys.stdin.readline().rstrip())

for i in range(C):
    count = 0
    N = list(map(int, sys.stdin.readline().split()))
    avg = (sum(N) - N[0])/N[0]
    # print(f'{round(avg,5)}%')
    # print(avg)

    for i in range(N[0]):
        if N[i+1] > avg:
            count+=1

    a = count / N[0] * 100
    # print(f'{round(count/N[0]*100,3)}%') 이게 틀리네 ㅂㄷ
    print(f'{"%.3f"%a}%')