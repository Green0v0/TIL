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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for i in tokenList:
        if i not in prec.keys() and i != ')':
            postfixList.append(i)
        else:
            if opStack.size() == 0 or i == '(':
                opStack.push(i)
            elif i == ')':
                while True:
                    if opStack.peek() != '(':
                        postfixList.append(opStack.pop())
                    else:
                        opStack.pop()
                        break
            else:
                if prec[opStack.peek()] >= prec[i]:
                    while not opStack.isEmpty():
                        postfixList.append(opStack.pop())
                    opStack.push(i)
                else:
                    opStack.push(i)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList

def postfixEval(tokenList):
    ppStack = ArrayStack()
    answer = 0
    prec = '+-*/'
    for i in tokenList:
        if str(i) in prec:
            second = ppStack.pop()
            first = ppStack.pop()
            if i == '+':
                answer = first+second
            elif i == '-':
                answer = first-second
            elif i == '*':
                answer = first*second
            else:
                answer = first//second
            ppStack.push(answer)
        else:
            ppStack.push(i)
    while not ppStack.isEmpty():
        answer = ppStack.pop()
    return answer
print(infixToPostfix(splitTokens('7 * (9 - (3+2))')))
print(postfixEval(infixToPostfix(splitTokens('7 * (9 - (3+2))'))))
print(eval('7 * (9 - (3+2))'))

def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val

# print(eval('70 * (9 - (3+2))'))