# stack
def solution(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
            continue
        if stack[-1] == i:
            stack.pop()
        else: # 어떻게 이 부분을 까먹니! 담에는 좀 더 꼼꼼히 살펴보자
            stack.append(i)
            
    return 0 if stack else 1

print(solution('baabaa'))
print(solution('zzz'))