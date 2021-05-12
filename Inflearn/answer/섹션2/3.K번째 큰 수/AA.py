# 1<N<100
import sys
N,k = map(int, sys.stdin.readline().split())
li = list(map(int,sys.stdin.readline().split()))
a = []
for i in range(len(li)):
    for j in range(len(li)):
        for t in range(len(li)):
            if i!=j and j!=t and i!=t:
                a.append(li[i]+li[j]+li[t])
a = set(a)
a = list(a)
a.sort()
print(a[-k])