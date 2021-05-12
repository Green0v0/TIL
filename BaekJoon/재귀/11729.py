import sys
N = int(sys.stdin.readline().rstrip())
circle = []
for i in range(N,0,-1):
    circle.append(i)
# print(circle)
place = [1,2,3]
def distence(start, end):
    pass

# 다른 풀이
def hanoi(disk, start, mid, end):
    if disk == 1:
        print(start, end)
    else:
        hanoi(disk - 1, start, end, mid)
        print(start, end)
        hanoi(disk - 1, mid, start, end)

total_disk = int(input())
total_mvmt = 0

for disk in range(total_disk):
    total_mvmt = total_mvmt * 2
    total_mvmt += 1

print(total_mvmt)
hanoi(total_disk, 1, 2, 3)

# 다른 풀이 2
n = int(input())
def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, c)
        hanoi(n - 1, b, a, c)
sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
print(sum)
hanoi(n, 1, 2, 3)

# 다른 풀이 3
# hanoi function def
def hanoi(n,a,b,c):
    if n==1:
        move.append([a,c])
    else:
        hanoi(n-1,a,c,b)
        move.append([a,c])
        hanoi(n-1,b,a,c)
move = [] # 이동 경로를 담을 list
hanoi(int(input()),1,2,3) # function 실행
print(len(move)) # 이동 횟수
print("\n".join([' '.join(str(i) for i in row) for row in move])) # 이동 경로 출력

# https://leedakyeong.tistory.com/entry/%EB%B0%B1%EC%A4%80-python-11729%EB%B2%88-%ED%95%98%EB%85%B8%EC%9D%B4-%ED%83%91-%EC%9D%B4%EB%8F%99-%EC%88%9C%EC%84%9Chanoi-top-in-python