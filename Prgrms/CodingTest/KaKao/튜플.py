# 순서가 있음
def solution(s):
    s = s.replace('{','[',s.count('{'))
    s = s.replace('}',']',s.count('}'))
    s = sorted(eval(s), key=lambda x: len(x))#[[2], [2, 1], [2, 1, 3], [2, 1, 3, 4]]
    result = []
    for i in s:
        set_i = set(i)
        if len(result) == 0:
            result += i
        else:
            set_result = set(result)
            add = list(set_i - set_result)
            result += add

    return result

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))

# 다른 사람 풀이
def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer
