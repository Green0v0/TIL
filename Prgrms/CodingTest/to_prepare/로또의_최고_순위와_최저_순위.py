"""
이때, 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 return 하도록 solution 함수를 완성해주세요.
"""
def solution(lottos, win_nums):
    # 0은 모르는 번호
    answer = [0, 0] # min, max
    for i in win_nums:
        if i in lottos:
            answer[0] += 1
    answer[1] = answer[0] + lottos.count(0)

    # 등수로 변환
    answer = sorted(list(map(lambda x: 7-x if x!=0 else 6, answer)))

    return answer

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))

# 다른 사람 풀이
def solution1(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]