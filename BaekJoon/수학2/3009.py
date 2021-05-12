import sys
X = []
Y = []
for __ in range(3):
    x,y = map(int, sys.stdin.readline().split())
    if x in X:
        X.remove(x)
    else:
        X.append(x)
    if y in Y:
        Y.remove(y)
    else:
        Y.append(y)

print(*X, *Y)

# 다른 풀이
import sys
x1,y1,x2,y2,x3,y3 = list(map(int,sys.stdin.read().split()))
X = [x1,x2,x3]
Y = [y1,y2,y3]
#print(X,Y)
for i in range(3):
    if X.count(X[i]) == 1:
        a=X[i]
    if Y.count(Y[i]) == 1:
        b=Y[i]
print(a,b)