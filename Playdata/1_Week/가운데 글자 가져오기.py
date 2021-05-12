def solution(s):
    answer = ''
    if len(s)%2==0:
        answer = s[len(s)//2-1:len(s)//2 +1]
    else:
        answer = s[len(s)//2]
    return answer
    # return str[(len(str)-1)//2:len(str)//2+1]