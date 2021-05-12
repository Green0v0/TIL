import sys
T = int(sys.stdin.readline().rstrip())
N = list(map(int, sys.stdin.readline().split()))
count = 0
for i in N:
    if i>=3:
        li = []
        for j in range(2,i):
            if i%j==0:
                li.append(0)
            else:
                li.append(1)
        if all(li) == True:
            count += 1
    elif i ==2:
        count += 1

print(count)

# 다른 풀이 1
Case = int(input())
num_list = list(map(int, input().split(' ')))
res_counting = 0
for i in num_list:
    cnt = 0
    if(i == 1):
        continue
    for j in range(2, i + 1):
        if(i % j == 0):
            cnt += 1
    if(cnt == 1):
        res_counting += 1
print(res_counting)

# 다른 풀이 2
num_count = int(input())
num_list = list(map(int, input().split(' ')))
res = 0

if len(num_list) == num_count:  # 첫 입력 수와 리스트의 갯수가 일치할때만 작동
    for i in num_list:  # 리스트를 순차적으로 순환
        count = 0  # 소수는 1과 자기자신으로만 나뉘는수 (수를 세기위한 count)
        for j in range(1, i + 1):  # 1부터 리스트의 수까지 진행
            if i % j == 0:  # i가 j로 나누어 진다면
                count += 1  # 나뉘는수 +1 증가
        if count == 2:  # 나뉘는수가 2개다 = 소수
            res += 1  # 리스트의 i항은 소수이다.
print(res)

# 다른 풀이 3 : 에라토스테네스의 체를 사용한 코드
import math

num_count = int(input())
num_list = list(map(int, input().split(' ')))
natural_num = list(range(2, 1001))  # 자연수 범위를 정한다.(소수는 1이상인 정수이기때문에 1은 뺀상태)
count = 0

if len(num_list) == num_count:
    for i in range(2, math.ceil(math.sqrt(1000))):  # p²≥100인 p의 배수(p를 제외한)까지만 지우면 된다.
        for j in natural_num:
            if j / i == 1:  # 자기 자신으로 나뉘는것은 제외
                pass
            elif j % i == 0:  # 그 이외에 나뉘는 수가 존재하면
                natural_num.remove(j)  # 그 수는 정수 리스트에서 제거
for k in num_list:
    if k in natural_num:  # num_list에 natural_num이랑 중복되는 수가 있다면 count +1
        count += 1
print(count)


