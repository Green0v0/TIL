# 셀프 넘버
# for i in range(1,100):
#     for j in range(1,100):
#         A = i
#         B = j
#         # AB = 10 * A + B
#         str_AB = str(A)+str(B)
#         AB = int(str_AB)
#         if 100 - (A+B) == AB:
#             print(A)
#             print(B)

li = list(range(1,100))
n_list = []

for n in range(1,100):
    if n < 10:
        n = n + n//1 + n%1
    else:
        n = n + n//10 + n%10
        if n > 100:
            break
    n_list.append(n)
# print(n_list)

# final = []
for i in range(1,100):
    final= n_list.count(i)
    if final == 0:
        print(i)

# 제출 -> 맞았ㄴ..ㅔ..

def function(n):
    str_n = list(map(int,str(n)))
    for i in range(len(str_n)):
        n = n + str_n[i]
    return n

def self_num(length):
    li = []
    for i in range(length):
        li.append(function(i))
        final = li.count(i)
        if final == 0:
            print(i)

def self_num1():
    li = []
    for n in range(1,10000):
        str_n = list(map(int,str(n)))
        for i in range(len(str_n)):
            n = n + str_n[i]
        li.append(n)
    for i in range(1,10000):
        final = li.count(i)
        if final == 0:
            print(i)
self_num1()

# 밍듀풀이
# set은 차집합 가능
def d(n):
    m = n
    for i in str(n):
        m += int(i)
    return m

list_a = []
for i in range(10000):
    list_a.append(d(i))

list_b = []
for i in range(10000):
    list_b.append(i)

s1 = set(list_a)
s2 = set(list_b)

self_numbers = list(s2-s1)
self_numbers = sorted(self_numbers)

for i in self_numbers:
    print(i)