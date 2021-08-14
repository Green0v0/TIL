import sys
dic = {'(': ')',
       '[': ']'}
while True:
    stack = []
    sentence = sys.stdin.readline().rstrip()
    if sentence == '.':
        break
    for s in sentence:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')' or s == ']':
            if not stack:
                print('no')
                break
            elif dic[stack[-1]] == s:
                stack.pop()
            else:
                print('no')
                break
    else:
        if stack:
            print('no')
        else:
            print('yes')