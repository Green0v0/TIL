from itertools import combinations
def solution(number, k):
    # if max(map(int,number[:k])) < int(number[k]):
    #     return number[k:]
    # number = list(map(int, number))
    # cnt = k
    # while cnt > 0:
    #     number.pop(number.index(min(number[:k])))
    #     cnt -= 1
    # return ''.join(list(map(str,number)))
    # 다른 방법, 경우의 수
    # if max(map(int, number[:k])) < int(number[k]):
    #     return number[k:]
    # n = number.index(max(number[:k]))
    # number = number[n:]
    # candidate = list(combinations(number,len(number) - (k-n)))
    # candidate.sort(reverse=True)
    # return ''.join(candidate[0])
    # 다른 방법 2, stack
    stack = []
    # cnt = k
    # for n in range(len(number)):
    #     if cnt == 0:
    #         stack.extend(number[n:])
    #         break
    #     if not stack:
    #         stack.append(number[n])
    #         continue
    #     if stack[-1] < number[n]:
    #         stack.pop()
    #         cnt -= 1
    #         stack.append(number[n])
    #     else:
    #         stack.append(number[n])
    for i in number:
        while stack and i > stack[-1]:
            if k > 0:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(i)
    if k > 0:
        for i in range(k):
            stack.pop()
    answer = ''.join(stack)
    return answer
# print(solution("1924",2))
# print(solution("1231234",3))
print(solution("4177252841",4))
# print(solution("4177852841",4))