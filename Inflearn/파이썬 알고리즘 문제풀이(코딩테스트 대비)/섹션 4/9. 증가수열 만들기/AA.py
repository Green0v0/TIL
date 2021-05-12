import sys
N = int(sys.stdin.readline().rstrip())
su=list(map(int,input().split()))
tmp=0; cnt=0; st=''
# print(su) [2, 4, 5, 1, 3]
while tmp<su[0] or tmp<su[-1]:
    # print(su)
    if tmp<su[0]<su[-1]:
        tmp=su[0]
        cnt+=1
        st+='L'
        del su[0]
    elif su[0]>su[-1]>tmp:
        tmp=su[-1]
        cnt+=1
        st+='R'
        su.pop()
    elif tmp<su[0]:
        tmp=su[0]
        cnt+=1
        st+='L'
        del su[0]
    elif tmp<su[-1]:
        tmp = su[-1]
        cnt += 1
        st += 'R'
        su.pop()
print(cnt)
print(st)