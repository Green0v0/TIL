import sys

li = []
for i in range(10):
    A = int(sys.stdin.readline().rstrip())
    li.append(A % 42)

set_li = set(li)
count = len(set_li)
print(set_li)
print(count)

# 다른 풀이
B = 42
result_set = set([])
for i in range(10):
     result_set.add(int(input())%B)
print (len(result_set))