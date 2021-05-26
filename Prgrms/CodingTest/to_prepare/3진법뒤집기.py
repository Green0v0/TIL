def solution(n):
    answer = ''
    while n > 0:
        a, b = n // 3, n % 3
        answer += str(b)
        n = a
    # 0021
    result = 0
    for i in range(len(answer)):
        result += (3**i)*int(answer[::-1][i])

    return result

print(solution(125))

# 다른 사람 풀이
def solution2(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    # 10진수는 int로 하면 됨!
    answer = int(tmp, 3)
    return answer