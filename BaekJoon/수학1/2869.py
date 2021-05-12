import sys
import math
A, B, V = map(int, sys.stdin.readline().split())
# 시간초과
# temp = 0
# day = -1
# while temp != V:
#     temp += (A-B)
#     day += 1

# 틀렸습니다.
# day = V//(A-B) -1
# if V%(A-B) ==0:
#     day = V//(A-B) -1
# else:
#     day = V//(A-B)

day = (V -(A-B))/(A-B)
day = math.ceil(day)
print(day)

# 다른 풀이
# 하지만 목표지점에 도달 했을때는 미끄러지지 않으므로 v - b만큼 올라가게 되는 것이다.
# 마지막날에는 잠자는걸 고려하지 않는 다는 부분을 생각해주어야 합니다.
A, B, V = list(map(int, input().split()))
print((V - B - 1) // (A - B) + 1)

# 다른 풀이 2
a,b,v = map(int,input().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)	#삼항연산자