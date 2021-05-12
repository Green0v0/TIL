from collections import Counter
import copy
def solution(l, v):
    answer = 0
    result = copy.deepcopy(v)
    dic = {i:0 for i in range(l+1)}
    print(dic)
    while answer < 4:
        answer += 1
        for i in range(len(v)):
            for j in range(-answer, answer + 1):
                if 0 <= v[i] + j <=l:
                    # result.append(v[i] + j)
                    dic[v[i] + j] += 1
        # if 0 not in Counter(result).values():
        dic_v = list(dic.values())
        if dic[0] >= 0 and 0 not in dic_v[1:]:
            break

        dic = {i:0 for i in range(l+1)}

    return answer + 1


print(solution(15, [15,5,3,7,9,14,0]))
# print(solution(5,[2,5]))
