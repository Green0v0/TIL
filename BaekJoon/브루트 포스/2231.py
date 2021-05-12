import sys
N = int(sys.stdin.readline().rstrip())
def divide(N):
    # 자리수 파악
    length = len(str(N))
    return 10**(length-1)

# list_N = list(map(int,str(N)))
start = divide(N) - (divide(N)//2)
generator = []

while start != N:
    list_start = list(map(int,str(start)))
    temp = start + sum(list_start)
    if temp == N:
        generator.append(start)
    start+=1

if len(generator) == 0:
    print(0)
else:
    # print(generator)
    print(min(generator))

# 다른 풀이 1
# 다른 것들 다 별 차이 없음
# 분해합 식 + break 한 방식 생각의 차이 기억하기.
# 브루트포스 문제는 단순 무식하게 접근한다.
N = int(input())
print_num = 0
for i in range(1, N+1):
    div_num = list(map(int, str(i)))
    sum_num = i + sum(div_num)
    if(sum_num == N):
        print_num = i
        break
print(print_num)