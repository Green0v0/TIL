def solution(clothes):
    key = list(zip(*clothes))[1]
    dic = {k:[] for k in key}
    for value, k in clothes:
        dic[k].append(value)
    total = 1
    for t in list(map(lambda x: len(x) + 1, dic.values())):
        total *= t
    return total - 1

def solution1(clothes): # https://velog.io/@djagmlrhks3/Algorithm-Programmers-%EC%9C%84%EC%9E%A5-by-Python
    answer = 1
    total = dict()
    for clothe in clothes:
        if clothe[1] not in total:
            total[clothe[1]] = 1
        else:
            total[clothe[1]] += 1
    if len(total) == 1: #의상의 종류(key)가 하나일 경우 value값 리턴
        return len(clothes)
    else: #의상의 종류(key)가 하나 이상일 경우 value+1 값 곱하기
        for i in total.values():
            answer *= i+1
    return answer - 1 # 모든 의상을 입지 않는 경우 제외(-1)
print(solution([["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])) #["yellowhat", "headgear"],
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])) #["yellowhat", "headgear"],
print(solution([["yellowhat", "headgear"]]))
