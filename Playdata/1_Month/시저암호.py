# 풀이 1
def solution(s,n):
    start = list(s)
    answer = ''
    for i in range(len(start)):
        if ord(start[i]) == 32:
            start[i] = ord(start[i])
        else:
            start[i] = ord(start[i])+n
        if (chr(start[i] - n).isupper() and 90<start[i]) or (chr(start[i] - n).islower() and start[i]>122):
            start[i] = start[i] - 26
        start[i] = chr(start[i])
    for j in start:
        answer+=j
    return answer
# 다른 사람 풀이
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)