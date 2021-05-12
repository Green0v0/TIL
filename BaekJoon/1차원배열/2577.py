import sys
A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())

ABC = A*B*C
map_ABC = list(map(int,list(str(ABC))))
# list_ABC = list(str(ABC))
li = [0,0,0,0,0,0,0,0,0,0]

for idx in map_ABC:
    li[idx] += 1

for i in range(10):
    print(li[i])

# 다른 방법
# 결과값을 배열로 만들기
ABC = str(ABC)
# count()써서 개수 구하기
for i in range(0, 10):
    print(ABC.count(str(i)))
