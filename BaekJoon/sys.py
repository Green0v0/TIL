import sys

# input1, input2 = int(sys.stdin.readline().split())
# print(input1+input2)

# for x in sys.stdin.readline().rsplit():
#     print(x)

# a = list(map(int, sys.stdin.readline().split()))
# print(a)

# li = []
#
# for line in sys.stdin:
#     li.append(tuple(map(int, line.strip().split())))
#     print(li)

# a = sys.stdin.readline().split()
# for line in sys.stdin:
#     print(line)

# for a in sys.stdin.readline().split():
#     print(a)

# for line in sys.stdin:
#     li = []
#     li.append(list(map(int, line.strip().split())))
#     print(li)
#     print(li[0][0] + li[0][1])

# a = list(map(int, sys.stdin.readline().split()))
# print(a[0]+a[1])

# T = sys.stdin.readline().split()
# # T = int(T)
# print(type(T))
# T = int(T[0])
# print(type(T))

# for line in sys.stdin.readline().split():
# a, b = sys.stdin.readline().rsplit()
# c = int(a)
# d = int(b)
# print(d+c)

# for count in range(T):
#     a, b = sys.stdin.readline().split()
#     a = int(a)
#     b = int(b)
#     print(a+b)

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)

n = int(sys.stdin.readline())
for i in range(n):
    arr = sys.stdin.readline().split()
    print(int(arr[0])+int(arr[1]))

# 런타임 에러 코드들
import sys
for line in sys.stdin:
    li = []
    li.append(list(map(int, line.strip().split())))
    print(li[0][0] + li[0][1])

import sys
a = list(map(int, sys.stdin.readline().split()))
print(a[0]+a[1])

import sys
a, b = sys.stdin.readline().split()
c = int(a)
d = int(b)
print(d+c)

# 참고
# li = []
#
# for line in sys.stdin:
#     li.append(tuple(map(int, line.strip().split())))
#     print(li[0][0])

for line in sys.stdin:
    a, b = list(map(int, line.strip().split()))
    print(a + b)

# line = sys.stdin.readline() # \n 이 포함된 상태
# spli = sys.stdin.readline().split()
# mapspli = map(int,sys.stdin.readline().split())
# listmapspli = list(map(int,sys.stdin.readline().split()))
# stri = sys.stdin.readline().rstrip()
# print(line)
# print(spli)
# print(mapspli)
# print(listmapspli)
# print(stri)
# print(type(line))
# print(type(spli))
# print(type(mapspli))
# print(type(listmapspli))
# print(type(stri))