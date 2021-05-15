def psolution(s):
    slist = list(map(int,s.split()))
    smin =str(min(slist))
    smax =str(max(slist))
    result = smin+' '+smax
    return result

# 다른 풀이
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))

print(solution('1 2 3 4'))
print(solution('-1 -2 -3 -4'))
