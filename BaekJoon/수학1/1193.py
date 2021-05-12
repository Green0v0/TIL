import sys
X = int(sys.stdin.readline().rstrip())

# 코드 줄이기
def find(X):
    a = 1
    b = 1
    first = [1, 1]
    li = [first]
    x = 1
    if X == 1:
        li = [first]

    while x != X:
        if (a+b)%2 == 0:
            for i in range(a+b,0,-1):
                li.append([a+b+1-i,i])
                if len(li) == X:
                    break
            a = a+1
        elif (a+b)%2 == 1:
            for i in range(a+b,0,-1):
                li.append([i,a+b+1-i])
                if len(li) == X:
                    break
            b = 1+b
        if len(li) == X:
            break

        x += 1
    print(li)
    result = li.pop()
    print(f'{result[0]}/{result[1]}')

find(X)

# 2번째 풀이
import sys
X = int(sys.stdin.readline().rstrip())
a = 1
b = 1
# # 1,3,6,10 = n(n+1)/2

num = 0
for i in range(1,X+1):
    if X <= i*(i+1)//2:
        num = i
        # print(i)
        break
ex = []
for idx in range(num):
    ex.append([idx + 1, num - idx])
if num%2==0:
    ex = sorted(ex,key=lambda x : x[1])

# print(ex[num*(num+1)//2-X])
result = ex[num*(num+1)//2-X]
print(f'{result[0]}/{result[1]}')

# 다른 풀이
stage, key_X = 1,1
while key_X+stage <=X:
    key_X += stage
    stage += 1
step = X - key_X
x, y = step + 1, stage-step
if stage % 2 == 0:
    print('{}/{}'.format(x,y))
else:
    print('{}/{}'.format(y,x))
# 다른 풀이 2
line = 1
while X > line:
    X -= line
    line += 1
if line % 2 == 0:
    a = X
    b = line - X + 1
else:
    a = line - X + 1
    b = X
print(a, '/', b, sep='')