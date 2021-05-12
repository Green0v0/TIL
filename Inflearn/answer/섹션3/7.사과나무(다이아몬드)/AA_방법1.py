import sys
N = int(sys.stdin.readline().rstrip())
# 순환하는 리스트 a
# a = [i+2 if i<N else i-2 for _ in range(N)]
i = 1
a = []
while i < N:
    a.append(i)
    i+=2
    if i >= N:
        a.append(i)
        rev = list(reversed(a[0:N//2]))
        a = a + rev
# 출발지점
b = [(N-a[j])//2 for j in range(N)]

# cnt 2개 x축, y축
cnt_y = 0

li =[]
total = 0
for t in range(N):
    li = list(map(int,sys.stdin.readline().split()))
    # b[t], a[t]
    index = b[t]
    for _ in range(a[t]):
        total += li[index]
        # print(li[index])
        index += 1

print(total)
# list에 저장하는 코드 지양하기
# for i in range(N):
#     li.append(list(map(int,sys.stdin.readline().split())))
