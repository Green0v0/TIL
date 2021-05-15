def check(a, b, i):
    na = a // i
    nb = b // i
    return na, nb

def solution(N,a,b):
    cnt = 1
    repeat = 2
    while repeat != N:
        na, nb = check(a - 1, b - 1, repeat)
        if na == nb:
            break
        cnt += 1
        repeat *= 2
    return cnt

print(solution(8,4,7))
print(solution(8,1,4))

# 유사한 다른 풀이
def solution1(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer

# 다른 풀이
def solution2(n,a,b):
    return ((a-1)^(b-1)).bit_length()