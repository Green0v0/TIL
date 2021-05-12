import sys
a = list(input())
stack = []
cnt = 0 # (( 누적 숫자
answer = 0
past = ''
for x in a:
    if len(stack)==0:
        stack.append(x)
        cnt+=1
    elif x == ')':
        stack.pop()
        cnt-=1
        if cnt!=0:
            answer+=cnt
        elif cnt!=0 and past == x:
            answer+=1
        past = x
    else:
        cnt+=1
        stack.append(x)
    # print(cnt , answer)
print(answer)