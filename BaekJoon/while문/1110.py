import sys
import copy
# 참고
# list(map(int, list(str(15))))
# [1, 5]
N_str = sys.stdin.readline().rstrip()
N_int = int(N_str)
N = list(map(int, list(N_str)))
result = [0,0]
cycle = 0

# 틀린 코드
if N_int < 10 :
    N[0] = 0
    N.append(N_int)

# def N_sum_check():
#     if N_sum >= 10:
#         one = list(map(int, list(str(N_sum))))
#         result[1] = one[1]

while N != result :
    if cycle == 0:
        result = copy.deepcopy(N)
        N_sum = result[0]+result[1]
        result[0] = result[1]
        if N_sum >= 10:
            one = list(map(int, list(str(N_sum))))
            result[1] = one[1]
        else:
            result[1] = N_sum
        cycle = cycle + 1
    else :
        N_sum = result[0]+result[1]
        result[0] = result[1]
        if N_sum >= 10:
            one = list(map(int, list(str(N_sum))))
            result[1] = one[1]
        else:
            result[1] = N_sum
        cycle = cycle + 1

print(cycle)

# 정답 코드
# check = N_int
# new_num = 0
# temp = 0
# count = 0
# while True :
#     temp = N_int//10 + N_int%10
#     new_num = (N_int%10)*10 + temp%10
#     count += 1
#     N_int = new_num
#     if new_num == check :
#         break
# print(count)