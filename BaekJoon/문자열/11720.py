import sys
N = int(sys.stdin.readline().rstrip())
list_n = sys.stdin.readline().rstrip()

# int_n = list(map(int,list_n))
total = 0

# for i in int_n:
#     total = total + i

for i in list_n:
    total = total + int(i)

print(total)