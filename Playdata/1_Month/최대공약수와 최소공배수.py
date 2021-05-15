def solution(n, m):
    if n>m:
        n, m = m, n
    answer = []
    for i in range(1,n+1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
    # 최소공배수
    min_cal = max(answer)
    return [min_cal, (n//min_cal)*(m//min_cal)*min_cal]

# def gcdlcm(a, b):
#     c, d = max(a, b), min(a, b)
#     t = 1
#     while t > 0:
#         t = c % d
#         c, d = d, t
#     answer = [c, int(a*b/c)]

#     return answer