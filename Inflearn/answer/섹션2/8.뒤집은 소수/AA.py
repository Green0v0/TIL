# 뒤집는 함수 def reverse(x)
# 소수인지 확인하는 함수 def isPrime(x)
import sys

# def reverse(x):
    # x = list(str(x))
    # x.reverse()
    # # x = ['3','2']
    # rev = ''
    # for i in x:
    #     rev += i
    # rev = int(rev)
    # return rev

def reverse(x):
    res = 0
    while x>0:
        t = x % 10
        res = (res*10) + t
        x = x//10
    return res

# 소수인지 확인하는 함수 (에라토스테네스 체)
def isPrime(x):
    if x == 1:
        return False
    for i in range(2,x):
        if x%i == 0:
            prime = False
            break
    else:
        prime = True
    return prime

N = int(input())
li = list(map(int,input().split()))
for i in range(len(li)):
    if isPrime(reverse(li[i])):
        print(reverse(li[i]), end=' ')

