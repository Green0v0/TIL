import sys
# N = int(sys.stdin.readline().rstrip())
# li = []
# numbers = [1,1,2,2,2,3]
# numbers = [# 1,3,1,4,5,6,3,2]
numbers = [1,3,3,4,4,4]
se = set(numbers)
li = list(se)
final = 0
for i in li:
    co = numbers.count(i)
    # print(co)
    if co > 1:
        final = final+1
print(final)
# print(N-len(se))