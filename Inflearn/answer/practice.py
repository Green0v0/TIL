class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

S1='A+B*C-D'
def solution(S):
    opStack = ArrayStack()
    answer = ''
    for i in S:
        if i not in prec.keys() and i != ')':
            answer += i
        else:
            if opStack.size() == 0 or i == '(':  # 여는 괄호의 경우
                opStack.push(i)
            # elif 닫는 괄호가 나오는 경우 추가
            elif i == ')':
                while True:
                    if opStack.peek() != '(':
                        answer+=opStack.pop()
                    else:
                        opStack.pop()
                        break
            else:  # prec의 크기 비교
                if prec[opStack.peek()] >= prec[i]:
                    while not opStack.isEmpty():
                        answer += opStack.pop()
                    opStack.push(i)
                else:
                    opStack.push(i)
    while not opStack.isEmpty():
        answer+=opStack.pop()
    return answer
print(solution(S1))