import sys

H, M = map(int, sys.stdin.readline().split())

minus = M - 45

if minus < 0 :
    if H == 0:
        H = 23
    else:
        H = H - 1
    M = 60 + minus

else :
    M = minus

print(f'{H} {M}')

# 민주코드
h, m = map(int, input().split())
time = 60*h + m
if time-45 < 0:
    time = time + 60*24
h = (time-45)//60
m = (time-45)%60
print(h, m)