# 멀리 뛰기 1 or 2
# 1이나 2의 초합으로 4를 만들 수 있는 가짓수
def psolution(n):
    if n <= 3:
        return n%1234567
    else:
        return (solution(n-1)+solution(n-2))%1234567
# 더 빠른 답
def solution(n):
    if n<3:
        return n%1234567
    value1, value2 = 1,2
    for i in range(3, n+2):
        value1, value2 = value2, value1+value2
    return value1 % 1234567
# 다른 풀이
def jumpCase(num):
    a, b = 1, 2
    for i in range(2,num):
        a, b = b, a+b
    return b