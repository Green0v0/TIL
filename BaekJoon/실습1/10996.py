import sys
star = '*'
odd = ' *'
plus = '\n *'
N = int(sys.stdin.readline().rstrip())
group = (N+1)//2
repeat = group-1

if N % 2 != 0 :
    # 홀수이면
    for i in range(N):
        if N == 1:
            sen = star + odd * repeat + plus*0 + odd * (repeat-1)
        else :
            sen = star + odd * repeat + plus + odd * (repeat-1)
        print(sen)
else :
    # 짝수이면
    for i in range(N):
        sen = star + odd * repeat + plus + odd * repeat
        print(sen)

# 다른 풀이 1
num = int(input())
for i in range(num*2):
    if num==1:
        print('*')
        break
    for j in range(num):
        if (j+i)%2==0:
            print('*',end='')
        else:
            print(' ',end='')
    print('')

# 다른 풀이 2
count = int(input())
if count == 1:
    print('*')
else:
    if count % 2 == 0:
        a = '* ' * (count // 2)
        b = ' *' * (count // 2)
    else:
        a = '* ' * (count // 2) + '*'
        b = ' *' * (count // 2)

    for _ in range(count):
        print(a)
        print(b)