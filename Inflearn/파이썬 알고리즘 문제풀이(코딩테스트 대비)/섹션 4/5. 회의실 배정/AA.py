import sys
n = int(sys.stdin.readline().rstrip())
to = []
for i in range(n):
    s, e = map(int,sys.stdin.readline().split())
    to.append((s,e))
# print(to)
to.sort(key=lambda x : (x[1],x[0]))
# print(to)
ep=0
cnt=0
for s,e in to:
    if ep<=s:
        cnt+=1
        ep=e
print(cnt)