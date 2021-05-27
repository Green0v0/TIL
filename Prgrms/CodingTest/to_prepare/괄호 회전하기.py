# 올바른 괄호인지 확인하는 함수
def check(s):
    dic = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if i in dic.values():
                stack.append(i)
                continue
            elif stack[-1] == dic[i]:
                stack.pop()
                continue
            else:
                stack.append(i)
    return True if not stack else False


# 괄호를 한 칸씩 회전
def solution(s):
    cnt = 0
    for i in range(len(s)):
        s = s[1:] + s[:1]
        if check(s):
            cnt += 1
    return cnt
# print(solution('[](){}'))
print(solution("}]()[{"))