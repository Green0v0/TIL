"""
두 집합 A, B 사이의 자카드 유사도 `J(A, B)`는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의된다.

입력으로 들어온 문자열은 `두 글자`씩 끊어서 다중집합의 원소로 만든다.
이때 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다.
예를 들어 "ab+"가 입력으로 들어오면, "ab"만 다중집합의 원소로 삼고, "b+"는 버린다.
다중집합 원소 사이를 비교할 때, 대문자와 소문자의 차이는 무시한다. "AB"와 "Ab", "ab"는 같은 원소로 취급한다.

이를 다루기 쉽도록 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력
"""
from collections import Counter
from itertools import combinations
from itertools import permutations
import copy

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    C_str1 = Counter([str1[i:i + 2] for i in range(0,len(str1) - 1) if str1[i:i + 2].isalpha()])
    C_str2 = Counter([str2[i:i + 2] for i in range(0,len(str2) - 1) if str2[i:i + 2].isalpha()])

    cnt1 = sum((C_str1 - (C_str1-C_str2)).values())
    for s2, v2 in C_str2.items():
        if C_str1[s2]: # s2 단어가 있다면
            if C_str1[s2] < v2:
                C_str1[s2] = v2
        else: # s2 단어가 없다면
            C_str1[s2] =  v2

    cnt2 = sum(C_str1.values())

    return int(cnt1/cnt2*65536) if cnt2 != 0 else 65536

print(solution('FRANCE','french'))
# print(solution('handshake','shake hands'))
# print(solution('hahahaeeka','haeekakaeh'))
# print(solution('aa1+aa2','AAAA12'))

# 다른 사람 풀이
def solution(str1, str2):

    list1 = [str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]
    list2 = [str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]

    tlist = set(list1) | set(list2)
    res1 = [] #합집합
    res2 = [] #교집합

    if tlist:
        for i in tlist:
            res1.extend([i]*max(list1.count(i), list2.count(i)))
            res2.extend([i]*min(list1.count(i), list2.count(i)))

        answer = int(len(res2)/len(res1)*65536)
        return answer

    else:
        return 65536