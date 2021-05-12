items = ['*','-','+']
from itertools import permutations
expression = '100-200*300-500+20'
ex = expression.split('+')
# for i in ex:
#     result = i.split('*')
#     print(result)
# print(ex[1])
# print(eval(ex[1]))
    # 중복포함
check = list(permutations(items, 3))
# [('*', '-', '+'), ('*', '+', '-'), ('-', '*', '+'), ('-', '+', '*'), ('+', '*', '-'), ('+', '-', '*')]
answer = 0
expression = '100-200*300-500+20'
for i in range(len(check)):
    ex = expression.split(check[i][2])
    print(ex)
    for j in ex:
        result = j.split(check[i][1])
        for k in range(len(result)):
            result[k] = eval(result[k])
        print(result)
    print('====')