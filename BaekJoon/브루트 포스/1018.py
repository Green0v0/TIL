import sys
M, N = map(int,sys.stdin.readline().split())
plate = []
for i in range(M):
    a = list(sys.stdin.readline().rstrip())
    plate.append(a)
# print(M,N)
# print(plate)
# for i in range(M):
#     print(plate[i])

# 기본 체스판 비교모델 2개 생성
def chess(color):
    list_1 = [color]
    for i in range(1,8):
        if list_1[i-1] == 'W':
            list_1.append('B')
        elif list_1[i-1] == 'B':
            list_1.append('W')
    return list_1

if chess('W')[0] == 'W':
    pass
print(chess('W'))