import sys
N = int(sys.stdin.readline().rstrip())
check = '666'
n = 0
a = 600
while n != N:
    str_a = str(a)
    if check in str_a:
        n += 1
    a += 1

print(a-1)

# 다른 풀이 1
n = int(input(""))

num = 0
count = 0

while True:
    num += 1
    if '666' in str(num):
        count += 1
    if count == n:
        break

print(num)