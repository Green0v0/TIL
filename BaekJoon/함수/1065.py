import sys
x = int(sys.stdin.readline().rstrip())
li = []

# 함수 만들기
def check(list_n):
    ca = list_n[0] - list_n[1]
    for i in range(len(list_n)):
        try:
            if list_n[i] - list_n[i + 1] == ca:
                case = True
            else:
                case = False
        except:
            pass
    return case

def count(x):
    for n in range(1,x+1):
        list_n = list(map(int,str(n)))
        # print(list_n)
        if len(list_n) <= 2:
            li.append(n)
        else:
            # ca = list_n[0] - list_n[1]
            # for i in range(len(list_n)):
            #     try :
            #         if list_n[i] - list_n[i+1] == ca:
            #             case = True
            #         else:
            #             case = False
            #     except :
            #         pass
            case = check(list_n)
            if case == True:
                li.append(n)
    print(len(li))

count(x)

# 다른 풀이
def hn(n):
    if n < 10:
        return True
    ns = [int(c) for c in str(n)]
    d = ns[0] - ns[1]
    return all(ns[i] - ns[i+1] == d for i in range(len(ns)-1))
# all() 은 인자로 전달된 모든 값이 True 인지 아닌지를 확인 합니다
# any() 는 인자로 전달된 모든 값 중 하나라도 True 가 있는지 확인 합니다
# short-circuit evaluation and/or 연산을 함에 있어서 첫 번째 인수로 값을 평가하기에 충분하다면
# 두 번째 (또는 그 이후) 인수는 평가하지 않는 것을 의미합니다

n = int(input())
print(sum(1 for i in range(n) if hn(i+1)))