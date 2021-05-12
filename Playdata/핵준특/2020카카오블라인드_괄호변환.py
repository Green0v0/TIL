# '(' 의 개수와 ')' 의 개수가 같다면 이를 균형잡힌 괄호 문자열이라고 부릅니다.
#  '('와 ')'의 괄호의 짝도 모두 맞을 경우에는 이를 올바른 괄호 문자열
# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
#    단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#   4-3. ')'를 다시 붙입니다.
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#   4-5. 생성된 문자열을 반환합니다.

from collections import Counter
# 올바른 문자열인지 확인하는 함수
# def right(s):
#     stack = []
#     for i in s:
#         if len(stack) == 0:
#             stack.append(i)
#         elif stack[-1] == '(' and i == ')':
#             stack.pop()
#         else:
#             stack.append(i)
#
#     return True if not stack else False
#
# def solution(p):
#     answer = ''
#     # u, v 분리
#     for i in range(2, len(p), 2):
#         x = p[:i].count('(')
#         y = p[:i].count(')')
#         if x == y:
#             u = p[:i]
#             v = p[i:]
#             break
#     # 재귀
#     # 완료 조건이 중요 <- 변환시킨 p값이 올바른 괄호 문자열이면 stop
#     if right(u):
#         v = solution(v)
#     else: # right(u)가 False라면
#         u = u[1:len(u) - 1]
#         u = u[::-1]
#         v = '(' + solution(v) + ')' + u
#
#     # answer = u + v
#     # if len(answer) == len(p):
#     #     return answer
#
#     # return solution(answer)
#
# print(solution('()))((()'))

# notion
# 주어진 로직을 그대로 구현할 수 있는지 파악
# 재귀함수를 이해하고 작성할 수 있는지 파악
# 재귀함수 -> base case를 작성해야 한다.
def solution(p):
    # 입력이 빈 문자열인 경우, 빈 문자열을 반환
    if p == "":
        return p

    # 문자열을 u, v로 분리
    cnt, idx = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt == 0:
            idx = i
            break

    u, v = p[:idx+1], p[idx+1:]

    # u가 올바른 괄호 문자열이라면 v에 대해 1단계부터 다시 수행
    if u[0] == "(": # 이미 잘린 데이터인 상태에서 시작하는 부위가 여는 괄호면 올바른거임!
        return u + solution(v)

    # 4번 과정
    else:
        # 4-4 과정
        new_u = ""
        for i in u[1:-1]:
            if i == "(":
                new_u += ")"
            else:
                new_u += "("

        return "(" + solution(v) + ")" + new_u

print(solution("()))((()"))