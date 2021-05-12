import sys
A = int(sys.stdin.readline().rstrip())
li = []
for i in range(5):
    if (A - 5*i)%3 == 0 and A >= (5*i) :
        C = (A - 5*i)//3
        print(f'c의 값 : {C}')
        li.append(C)
        # print(i)
# print(min(li))
print(li)
#
# if (A - 5) % 3 == 0 and A >= (5):
#     C = (A - 5) // 3
#     print(f'c의 값 : {C}')

# 다른 풀이
n = int(input())

case_list = []
N_5 = n // 5

for i in range(N_5, -1, -1):
    n_5 = n-(i*5)
    if n_5%3 == 0:
        a = n_5//3
        b = i
        case_list.append(a+b)

if len(case_list) == 0:
    print(-1)
else:
    print(min(case_list))

# 다른 풀이 2
inp = int(input())
Box = 0
while True:
    if (inp % 5) == 0:
        Box = Box + (inp//5)
        print(Box)
        break
    inp = inp-3
    Box += 1
    if inp < 0:
        print("-1")
        break

# 다른 풀이 3
order = int(input())
three = 0
five = order//5
order %= 5

while five >=0:
    if order % 3 ==0:
        three = order//3
        order %= 3
        break
    five -= 1
    order += 5
print(order==0 and (three + five) or -1)