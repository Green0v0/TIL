def solution(n):
    # 2이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567로 나눔
    # 피보나치 수 구하기
    # 시간 초과
    # def fibo(x):
    #     if x <= 1:
    #         return x
    #     return fibo(x-2)+fibo(x-1)
    # return fibo(n)%1234567
    fibo = []
    for i in range(n+1):
        if i<=1:
            fibo.append(i)
        else:
            fibo.append(fibo[i-1]+fibo[i-2])
    return fibo[-1]%1234567

print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))

# 다른 풀이
def fibonacci(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a