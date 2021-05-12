def solution(n, s):
    if s // n == 0:
        return -1

    result = []
    while n != 0:
        m = s // n
        result.append(m)
        s -= m
        n -= 1

    return result

print(solution(2,9))
print(solution(2,1))
print(solution(2,8))