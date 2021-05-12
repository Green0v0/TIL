import sys
C = int(sys.stdin.readline().rstrip())
# test = list(sys.stdin.readline().rstrip())


for idx in range(C):
    test = list(sys.stdin.readline().rstrip())
    li = []
    count = 0
    for i in test:
        if i == 'O':
            count += 1
            li.append(count)
        else :
            count = 0
    print(sum(li))

# 다른 방법
t = int(input())

p = lambda x: x * (x + 1) // 2

for x in range(t):
    s = input()
    v = s.split('X')
    r = 0
    for x in v:
        r += p(len(x))
    print(r)