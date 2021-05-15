def solution(arr):
    answer = []
    for i in arr:
        if len(answer)==0:
            answer.append(i)
        else:
            if answer[-1] == i:
                continue
            else:
                answer.append(i)
    # answer = list(set(arr))
    return answer