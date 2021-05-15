def solution(n):
    # answer = 0
    # if n==1: return 4
    # for i in range(n//2+1):
    #     if i**2 == n:
    #         answer=(i+1)**2
    #         break
    #     else:
    #         answer=-1
    n = n**(1/2)
    if n%1==0:
        return (int(n)+1)**2
    else:
        return -1