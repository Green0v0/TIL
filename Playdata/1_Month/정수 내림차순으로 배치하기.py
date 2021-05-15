def solution(n):
    n = sorted(str(n),reverse=True)
    answer = ''
    for i in n:
        answer += i
    return int(answer)

    # ls = list(str(n))
    # ls.sort(reverse = True)
    # return int("".join(ls))