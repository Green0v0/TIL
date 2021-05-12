def solution(N):
    count = 1
    while N != 1:
        if N % 2 == 1:
            N = (N-1) // 2
            count += 1
        else:
            N = N // 2

    return count

# 이렇게 마지막 예시인 5000을 2로 나누어가며 나머지를 찾던 도중..
# 아 이건 주어진 N을 2진수로 바꾸면 나머지가 1인 경우는 1로 표시되겠구나..라는 것을 캐치할 수 있었다.
def othersolution(n):
    return bin(n).count('1')

solution(5)
solution(6)
solution(5000)