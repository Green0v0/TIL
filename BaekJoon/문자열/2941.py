import sys
# import string

# eng = list(string.ascii_lowercase)
lang = ['c=','c-','dz=','d-','lj','nj','s=','z=']

N = sys.stdin.readline().rstrip()

total = 0
replace_N = N

for i in lang:
    if i in N:
        total += 1
        replace_N = replace_N.replace(i,"")

print(len(replace_N)+total)

# c=c= 일때...
# 제 2 풀이
for i in lang:
    replace_N = replace_N.replace(i,"a")

# print(N)
# print(replace_N)
print(len(replace_N))