import sys

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

# EOF?
# 풀이1 (출처: https://home-body.tistory.com/258)
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break

# 풀이2 (출처 : https://hwiyong.tistory.com/m/208?category=844316 )
import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    print(a + b)

# 풀이3 (출처 : https://sinb57.tistory.com/entry/Python-3-10951-A-B-4 )
try:
    while 1:
        a, b = map(int, input().split())
        print(a + b)
except:
    exit()

# 풀이 4
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break