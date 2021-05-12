import sys
li = []
for i in range(9):
    li.append(int(sys.stdin.readline().rstrip()))

for i in range(9):
    if li[i] == max(li):
        print(max(li))
        print(i+1)
# print(li.index(max(li)) + 1)

# 다른 방법
from sys import stdin

vals = 0
idx = 0

while True:
    line = stdin.readline()
    if not line:
        break

    idx += 1
    if vals < int(line):
        vals = int(line)
        max_idx = idx

print(vals)
print(max_idx)

# 다른 방법 2
import sys

li = []
for x in range(0, 9):
  a = int(sys.stdin.readline())
  li.append(a)

print(max(li))
print(li.index(max(li)) + 1)
