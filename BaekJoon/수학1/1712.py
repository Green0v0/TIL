import sys
A,B,C = map(int,sys.stdin.readline().split())

if A/(C-B) >= 0 : # 조건의 차이인듯...
    n = A//(C-B)+1
else:
    n = -1

print(n)

# 다른 풀이
if (C<=B):
    n = -1
else:
    n = A//(C-B)+1
print(n)