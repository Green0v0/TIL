import sys
N = int(sys.stdin.readline().rstrip())
su=list(map(int,input().split()))
lt=0
rt=N-1
empty=[]
last=0;st=''
# while lt<=rt: # 종료조건 1번
#     empty.append((su[lt],'L'))
#     empty.append((su[rt],'R'))
#     empty.sort()
#     print(empty)
#     if empty[0][0]<last and empty[1][0]<last:
#         break
#     if last<=empty[0][0]:
#         st+=empty[0][1]
#         last=empty[0][0]
#         if empty[0][1]=='L':
#             lt+=1
#         else:
#             rt-=1
#     else:
#         st+=empty[1][1]
#         last=empty[1][0]
#         if empty[1][1]=='L':
#             lt+=1
#         else:
#             rt-=1
#     empty=[]
#
# print(st)
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
# 포인터로 써서 해보기
