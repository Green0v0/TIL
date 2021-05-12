import sys
N = int(sys.stdin.readline().rstrip())
li = list(map(int,sys.stdin.readline().split()))
def digit_sum(x):
    # len_x = len(str(x))
    list_x = list(map(int,str(x)))
    sum_x=0
    for i in list_x:
        sum_x = sum_x+i
    return sum_x

sum_li = []
for j in range(N):
    sum_li.append(digit_sum(li[j]))


print(li[sum_li.index(max(sum_li))])
