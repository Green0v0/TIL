# 그냥 계산..
def solution(A0, X, Y, M, n):
    # A[0] = A0
    # A[i] = (A[i - 1] * X + Y) MOD M (단, 0 < i < n)
    # 리스트 A에서 절대값의 차가 가장 작은 두 요소의 절대값의 차를 리턴하시오
    # DP : memoization
    A = [A0]
    for i in range(1,n):
        A.append(((A[i-1]*X)+Y)%M)

    A.sort()
    print(A)
    minus = float('inf')
    for j in range(1,n):
        minus = min(minus, abs(A[j]-A[j-1]))
    print(A)
    print(minus)
    return minus
print(solution(3,7,1,101,5))
print(solution(3,9,8,32,8))
print(solution(1,1221,3553,9889,11))
print(solution(1,1,1,2,10000))
