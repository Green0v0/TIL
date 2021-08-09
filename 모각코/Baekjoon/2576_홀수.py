import sys

total = []
for _ in range(7):
    num = int(sys.stdin.readline().rstrip())
    if num % 2 == 0:
        continue
    else:
        total.append(num)
if len(total) == 0:
    print(-1)
else:
    print(sum(total))
    print(min(total))