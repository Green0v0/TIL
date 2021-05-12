import sys
T = int(sys.stdin.readline().rstrip())

# n보다 작은 소수 리스트
def mini(n):
    pr = []
    a = [False, False]+[True]*(n-1)
    for i in range(2,n+1):
        if a[i]:
           pr.append(i)
           for j in range(2*i,n+1,i):
               a[j] = False
    return pr

for _ in range(T):
    ver = []
    add = []
    n = int(sys.stdin.readline().rstrip())
    # if n % 2 != 0: # 시간 초과 때문에 짝수만 가능하도록 했는데도 안대네...ㅠㅠ
    #     continue

    # for i in mini(n):
    #     for j in mini(n):
    #         if i >= j :
    #             if n == (i+j):
    #                 add.append([i,j])

    # 두 번 반복하는 for문을 줄임.
    for i in mini(n):
        if (n - i) in mini(n) and i>=(n-i):
            add.append([i, n - i])
    for li in add:
        ver.append(li[0]-li[1])
        if min(ver) == (li[0]-li[1]):
            print(f'{li[1]} {li[0]}')
# 내꺼 시간초과 ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ

# 풀이 1
# 92ms
# 주어진 n이 짝수이므로, n의 절반도 자연수이고, 그 수가 소수라면 이상적
# 소수가 아니라면 n의 절반에서 가까운 소수의 조합을 찾는 방법
# (n의 절반-x)+(n의 절반+x) = n 이므로 x를 증가시키다 보면 맞는 소수가 나올 것이다.
import sys
N = 10001
sieve = [True] * N
def prime_sieve(N):
    for i in range(2, N):
        if sieve[i]:
            for j in range(2*i, N, i):
                sieve[j] = False
prime_sieve(N)

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    idx = 0
    while True:
        if sieve[n//2 - idx] and sieve[n//2 + idx]:
            print(n//2 - idx, n//2 + idx)
            break
        idx += 1

# 풀이 2
# 1300ms
# 재료가 될 소수 생성
prime_ox = [True for _ in range(10001)]

for i in range(2, int((10001) ** 0.5)):
    if prime_ox[i] == True:
        for j in range(i + i, 10001, i):
            prime_ox[j] = False

prime_list = [i for i, j in enumerate(prime_ox) if j == True and i >= 2]

# 구한 소수를 더하여 골드바흐 리스트 안에 넣어주기 (여러개 가능)
goldbach = [[] for _ in range(10001)]

for i in range(len(prime_list)):
    for j in range(i, len(prime_list)):
        even_num = prime_list[i] + prime_list[j]
        if even_num % 2 == 0 and even_num <= 10000:
            goldbach[even_num].append([prime_list[i], prime_list[j]])

case = int(input())

for _ in range(case):
    num = int(input())
    answer = [0, 0]

    # 곱이 가장 큰 수: 가장 근접한 수
    for [i, j] in goldbach[num]:
        if i * j > answer[0] * answer[1]:
            answer[0] = i
            answer[1] = j

    print("%s %s" % (answer[0], answer[1]))