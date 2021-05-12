import sys
end = False
while end == False:
    primes = []
    n = int(sys.stdin.readline().rstrip())
    a = [False, False]+[True]*((2*n)-1)
    for i in range(2,(2*n)+1):
        if a[i]:
            primes.append(i)
            for j in range(i+i,(2*n)+1,i):
                a[j]=False
    primes = [i for i in primes if i > n]
    # print(primes)
    if n == 0:
        end = True
        break
    print(len(primes))

# 2가 왜 2번 출력되는 건지 = 해결
# 많은 양인건 범위지정을 해놓으면 되는 것이고 = 해결
# 13 -> [13, 17, 19, 13, 17, 19, 23] 7 왜죠? = while문 안에 primes 넣는 것으로 해결
# 13이 4개 나오는 것은 13을 포함하지 않아야 하는 것 때문 = 해결

# 다른 풀이 1
N = 123456 * 2 + 1
sieve = [True] * N
for i in range(2, int(N**0.5)+1):
    if sieve[i]:
        for j in range(2*i, N, i):
            sieve[j] = False

def prime_cnt(val):
    cnt = 0
    for i in range(val + 1, val * 2 + 1):
        if sieve[i]:
            cnt += 1
    print(cnt)

while True:
    val = int(input())
    if val == 0:
        break
    prime_cnt(val)