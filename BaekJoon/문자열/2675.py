import sys
N = int(sys.stdin.readline().rstrip())
S = []
for i in range(N):
    S.append(list(map(str,sys.stdin.readline().split())))

for li in S:
    list_s = list(li[1])
    repeat = int(li[0])
    for i in list_s:
        print(i*repeat,end='')
    print()

