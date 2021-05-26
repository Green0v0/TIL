# dp
# time out
def solution_1(n):
    me = [0,1,2,4,11,12,14,21,22,24,41]
    if n <= 10:
        return str(me[n])
    else:
        for i in range(11, n + 1):
            value = i // 3 - 1 if i % 3 == 0 else i // 3
            mod  = 4 if i % 3 == 0 else i % 3
            result = int(str(me[value]) + str(mod))
            me.append(result)
    return str(result)

# ver2
def solution(n):
    answer = ''

    # 1. 3으로 나눈 나머지에 매칭되는 숫자
    num_dict = {1: "1", 2: "2", 0: "4"}
    mok = 1 #몫
    na = 1  #나머지

    # 2. 몫이 0이 될 때까지 숫자를 만듦
    while mok != 0:
        mok = n // 3
        na = n % 3
        # 나머지가 0이라면 몫을 1 감소
        if na == 0:
            mok -= 1

        n = mok
        # 기존 answer에 앞부분에 하나씩 숫자를 붙여서 만듦
        answer = num_dict[na] + answer
    return answer

print(solution(28))
# print(solution(13))
# print(solution(14))
# print(solution(40))

# 다른 사람 풀이
def solution2(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1,3)
        return solution(q) + '124'[r]

# 다른 사람 풀이2
def change124(n):
    num = ['1','2','4']
    answer = ""


    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(change124(10))