import sys
N = int(sys.stdin.readline().rstrip())
li = list(map(int,sys.stdin.readline().split()))
total = 0
cnt = 0
for i in range(len(li)):
    if li[i] == 0:
        cnt = 0
    elif li[i] == 1:
        cnt += 1
    total += cnt

print(total)