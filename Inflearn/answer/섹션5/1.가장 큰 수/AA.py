import sys
from pythonds.basic.stack import Stack
s = Stack()
a, n = map(int,sys.stdin.readline().split())
a = [int(i) for i in str(a)]
cnt=0
answer = ''
while n != 0:
    for i in range(len(a)-n):
        print(a)
        if s.size() == 0:
            s.push(a[i])
            continue
        else:
            if s.peek()<a[i]:
                s.pop()
                s.push(a[i])
                cnt=i
            else:
                continue
        print(f'cnt={cnt}, n={n}')
        print(s.peek())
        print(answer)
    answer += str(s.peek())
    n = n-cnt
    if n>0:
        a = a[cnt+1:]
if n<=0:
    a = a[cnt+1:]
    for x in a:
        answer+=str(x)
