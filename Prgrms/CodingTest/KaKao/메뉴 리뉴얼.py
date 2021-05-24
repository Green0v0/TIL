"""
단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려고 합니다.
또한, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함하기로 했습니다.
"""
from itertools import combinations
def solution(orders, course):
    # course의 수만큼 combination 있는지 확인.
    dictionary = {}
    for order in orders:
        order = sorted(order)
        for cnt in course:
            for i in list(combinations(order, cnt)):
                dictionary[''.join(i)] = dictionary.get(''.join(i), 0) + 1

    dictionary = sorted(dictionary.items(), key= lambda x: (-len(x[0]), -x[1]))
    result = []
    max_v = -1
    len_k = 0
    for k, v in dictionary:
        if max_v == -1:
            len_k = len(k)
        max_v = max(max_v, v)
        if v >= 2 and max_v == v:
            result.append((k,v))
        if len_k != len(k):
            len_k = len(k)
    # print(list(*zip(result)))
    return sorted(list(list(zip(*result))[0]))

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))

# 다른 사람 풀이
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]

# 다른 사람 풀이 2
from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)