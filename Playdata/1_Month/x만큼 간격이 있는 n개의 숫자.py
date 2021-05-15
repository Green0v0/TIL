def solution(x, n):
    answer = []
    add_x = x
    while len(answer) != n:
        answer.append(add_x)
        add_x += x
    # return [x*(i+1) for i in range(n)]
    # return [i * x + x for i in range(n)]
    return answer