import sys
number = list(map(str,sys.stdin.readline().split()))
num1 = number[0]
num2 = number[1]

def sang(num):
    num_list = list(num)
    temp = num_list[0]
    num_list[0] = num_list[2]
    num_list[2] = temp
    return num_list

def num(list):
    num = list[0]+list[1]+list[2]
    int_num = int(num)
    return int_num

num1 = num(sang(num1))
num2 = num(sang(num2))
if num1 > num2:
    print(num1)
else :
    print(num2)

# 다른 풀이
import sys

A,B=map(str,sys.stdin.readline().split())
r_A=A[::-1]
r_B=B[::-1]
print(max(int(r_A),int(r_B)))

# 다른 풀이2
a,b=map(str,input().split())
c=list()
d=list()
c=[a[n] for n in range(len(a)-1,-1,-1)]
d=[b[n] for n in range(len(b)-1,-1,-1)]
e=int("".join(c))
f=int("".join(d))
if e>f: print(e)
else: print(f)