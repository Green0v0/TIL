def solution(n):
    li = [1,1]+[0 for i in range(n-1)]
    cnt=0
    for i in range(2,n+1):
        if li[i] == 0:
            # sosu.append(i)
            cnt+=1
        for j in range(i,n+1,i):
            li[j]=1
    # return len(sosu)
    return cnt

# 다른 풀이
# def solution(n):
#     num=set(range(2,n+1))

#     for i in range(2,n+1):
#         if i in num:
#             num-=set(range(2*i,n+1,i))
#     return len(num)