# 카운팅 정렬
# 각 숫자가 몇 번 등장하는지 세어줍니다.
# 등장 횟수를 누적합으로 바꿔줍니다.
import sys
# 입력된 숫자의 개수 N
N = int(sys.stdin.readline().rstrip())
# li는 입력된 숫자를 저장하는 배열
A = []
for i in range(N):
    A.append(int(sys.stdin.readline().rstrip()))

# 입력될 수 있는 숫자의 최대 크기를 의미합니다.
Max_num = 10000

# 0으로 초기화된 입력될 Max_num + 1 길이의 배열 count를 생성
count = [0]*(Max_num+1)
# countSum은 누적합을 저장하는 배열입니다.
countSum = [0]*(Max_num+1)

# 숫자 등장 횟수 세기
for i in range(N):
    count[A[i]] += 1

# 숫자 등장 횟수 누적합 구하기
countSum[0] = count[0]
for i in range(1,Max_num+1):
    countSum[i] = countSum[i-1]+count[i]

# B는 정렬된 결과를 저장하는 배열
B = [0]*(N+1)

for i in range(N-1,-1,-1):
    B[countSum[A[i]]] = A[i]
    countSum[A[i]] -= 1

# result = ""
# for i in range(1,N+1):
#     result += str(B[i])+" "
# print(B)
for i in B:
    if i == 0 :
        continue
    print(i)
# print(result)