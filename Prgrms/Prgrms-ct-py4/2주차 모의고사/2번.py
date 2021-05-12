# 괄호 stack
def solution(s):
    dict = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }
    stack = []
    for i in s:
        if i in dict.keys():
            stack.append(i)
        elif i in dict.values():
            if not stack or dict[stack.pop()] != i:
                return False

    # 스택이 남아있다면 False
    if stack:
        return False

    return True


print(solution("{{}}"))
print(solution("({})[]"))
print(solution("[)"))
print(solution("]()["))