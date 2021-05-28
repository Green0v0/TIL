def solution(citations):
    citations = sorted(citations, reverse=True)
    cit = citations[0]
    while cit >= 0:
        result = list(filter(lambda x: x>=cit, citations))
        if cit <= len(result):
            return cit
        cit -= 1

# print(solution([1,3,3,3,3,3,3,4,10,20,30,40]))
print(solution([1, 3, 5, 7, 9, 11]))#Test Case [1, 3, 5, 7, 9, 11] = 4
print(solution([0,0,0]))

# 다른 사람 풀이
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0