import sys
N = int(sys.stdin.readline().rstrip())

def cham(x):
    money = 0
    if x[0] == x[1] and x[1] == x[2] and x[0] == x[2]:
        money = 10000 + x[0]*1000
    elif x.count(x[0]) == 2 or x.count(x[1]) == 2:
        if x.count(x[0]) == 2 :
            money = 1000+x[0]*100
        elif x.count(x[1]) == 2:
            money = 1000 + x[1] * 100
    else:
        money = max(x)
        money = money*100
    return money

max_money = -2174000000
for i in range(N):
    li = list(map(int,sys.stdin.readline().split()))
    if max_money < cham(li):
        max_money = cham(li)
print(max_money)