"""
투 포인터
진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매

진열대 번호 순서대로 보석들의 이름이 저장된 배열 gems가 매개변수로 주어집니다.
이때 모든 보석을 하나 이상 포함하는 가장 짧은 구간을 찾아서 return 하도록 solution 함수를 완성해주세요.
가장 짧은 구간의 `시작 진열대 번호`와 `끝 진열대 번호`를 차례대로 배열에 담아서 return 하도록 하며,
만약 가장 짧은 구간이 여러 개라면 `시작 진열대 번호`가 가장 작은 구간을 return 합니다.
"""
def solution(gems):
    s = 0
    e = 1
    set_gems = set(gems)
    new_set = set(gems[s:e])

    while set_gems != set(new_set):
        e += 1
        new_set = set(gems[s:e])

    while len(set_gems - set(new_set)) == 0:
        s += 1
        new_set = set(gems[s:e])
        if s > e:
            break

    return [s,e]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(['a']))
print(solution(["AA", "AA", "AB"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]	))
print(solution(["DIA", "EM", "EM", "RUB", "DIA"])) #answer = [3, 5] output = [1, 4]

# 첫번째 풀이
# from collections import Counter
# def solution(gems):
#     s = 0
#     e = 1
#     dictionary = {i: 0 for i in list(set(gems))} #{'EMERALD': 0, 'RUBY': 0, 'SAPPHIRE': 0, 'DIA': 0}
#     for i in range(len(gems)):
#         result1 = Counter(gems[s:e])
#         if dictionary.keys() != result1.keys():
#             e += 1
#         else:
#             break
#     # result1 = Counter(gems[s:e])
#     # while dictionary.keys() != result1.keys():
#     #     e += 1
#     #     result1 = Counter(gems[s:e])
#
#     for j in range(e):
#         result2 = Counter(gems[s+j:e])
#         if dictionary.keys() == result2.keys():
#             x = s+j
#         else:
#             break
#     # result2 = Counter(gems[s:e])
#     # while dictionary.keys() == result2.keys():
#     #     s = s + 1
#     #     result2 = Counter(gems[s:e])
#
#     return [x+1,e]
def solution(gems):
    answer = []
    shortest = len(gems) + 1  # 현재 최단 구간 길이

    start_p = 0  # 구간의 시작점
    end_p = 0  # 구간의 끝 점 (보석을 체크하는 기준점)

    check_len = len(set(gems))  # 보석의 총 종류 수
    contained = {}  # 현재 구간에 포함된 보석들(종류: 갯수)

    while end_p < len(gems):  # 구간의 끝 점이 gems의 길이보다 작을 동안

        if gems[end_p] not in contained:  # 현재 끝 점의 보석이 contained에 없다면(이 종류가 처음 발견되었다면)
            contained[gems[end_p]] = 1  # dictionary에 추가
        else:
            contained[gems[end_p]] += 1  # 이미 있으면 dictionary에 +1

        end_p += 1  # 끝 점 증가

        if len(contained) == check_len:  # 현재 구간 내 보석의 종류의 갯수가 전체 종류의 갯수와 같다면 (현재 구간내 모든 종류가 다 있다면)
            while start_p < end_p:  # start_p 가 end_p 보다 같을 때까지 증가
                if contained[gems[start_p]] > 1:  # start_p에 해당하는 보석이 구간 내에 하나 이상 있다면
                    contained[gems[start_p]] -= 1  # 구간 내 보석 하나 감소(start_p 의 보석 뺄거니까)
                    start_p += 1  # start_p 증가

                elif shortest > end_p - start_p:  # 기존의 구간 최단거리보다 현재의 구간거리가 더 짧다면
                    shortest = end_p - start_p
                    answer = [start_p + 1, end_p]  # answer와 최단거리 갱신
                    break

                else:
                    break

    return answer
