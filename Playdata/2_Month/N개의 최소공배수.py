# 실수한 point
# 예를 들어 3개중에 2개만 공통 약수가 있어도 나누는 계산이 존재한다.
# 위의 문장을 고려하지 않는 함수임.
def psolution(arr):
    # i는 나눌 숫자
    for i in range(max(arr)//2+1,0,-1):
        # 각각 i로 나눈 리스트 update
        result = list(map(lambda x:x%i, arr))
        # print(result)
        if not any(result):
            # print(i)
            lsm = i
            break
    total = 1
    for j in arr:
        total*=(j//lsm)
    # print(answer)
    return total*lsm

def solution(arr):
    # 방법2 arr을 모두 곱하고 하나씩 제외하면서
    total = 1
    for i in arr:
        total*=i
    for y in range(min(arr),total+1,min(arr)):
    # for y in range(max(arr),total+1):
        result = list(map(lambda x: y%x, arr))
        if not any(result):
            return y

# gcd함수
import math
def nlcm(num):
    answer = num[0]
    for n in num:
        answer = n * answer // math.gcd(n, answer)
    return answer

print(solution([2,6,8,14]))
print(solution([1,2,3]))
print(solution([6,12,18]))
print(solution([2,7]))