"""
소수 구하기
- for 사용
- 에라토스테네스의 체
"""
def solution(n):
    li = [1,1]+[0 for i in range(n-1)]
    sosu = []
    for i in range(2,n+1):
        if li[i] == 0:
            sosu.append(i)
        for j in range(i,n+1,i):
            li[j]=1
    return len(sosu)
# set은 차집합이 가능하다는 특징을 사용한
# Solution 2
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
# 효율성이 더 뛰어남