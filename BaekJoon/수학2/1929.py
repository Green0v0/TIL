import sys
import math
M,N = map(int,sys.stdin.readline().split())
# 에라토스테네스의 체 방법이 아님.
for i in range(M,N+1):
    cnt = 0
    if i == 1:
        continue
    for j in range(1,i+1):
        if i%j == 0:
            cnt+=1
            if cnt>2:
                break
    if cnt == 2:
        print(i)

# 이건 왜 틀린거지..?
# 맞아따 (범위 조심)
a = [False, False] + [True]*(N-1)
primes = []

for i in range(2,N+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i,N+1,i):
            a[j] = False
for idx in primes:
    if idx >= M:
        print(idx)

# 방법 3
def get_primes(idx,n):
    # 구하고자 하는 수마큼 True를 갖는 리스트 생성
    is_primes = [True]*n
    # n의 최대 약수가 sqrt(n)이하이므로 계산한 후, 소숫점이 있을 경우 올림으로 최대 반복 횟수 계산
    max_length = math.ceil(math.sqrt(n))

    for i in range(2,max_length):
        # True일 경우, 소수
        if is_primes[i]:
            # i 이후 i의 배수들을 지워나감
            for j in range(i+i,n+1,i):
                is_primes[j] = False
    # 리스트의 True로 남아있는 인덱스(소수)를 추출
    return [i for i in range(idx,n) if is_primes[i]]
a = get_primes(M,N)
for i in a:
    print(i)

# 풀이 1
# 시간 초과요...??
def is_prime(num):
    if(num<=1):
        return False
    i = 2
    while i*i<=num:
        if num%i ==0:
            return False
    i += 1
    return True
for i in range(M,N+1):
    if(is_prime(i)):
        print(i)

# 풀이 2
# 출력 초과요....??
def isPrime(num):
    if num == 1:
        return False
    n = int(math.sqrt(num))
    for k in range(2, n+1):
        if num % k == 0:
            return False
        return True
# main
m, n = map(int, input().split())
for k in range(m, n+1):
    if isPrime(k) :
        print(k)
