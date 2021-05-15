def solution(answers):
    mem1 = [1,2,3,4,5]*2000
    mem2 = [2,1,2,3,2,4,2,5]*1250
    mem3 = [3,3,1,1,2,2,4,4,5,5]*1000
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    fi = 0
    for i in range(len(answers)):
        if mem1[i]==answers[i]:
            cnt_1+=1
        if mem2[i] == answers[i]:
            cnt_2 += 1
        if mem3[i]==answers[i]:
            cnt_3+=1
    an = [cnt_1, cnt_2, cnt_3]
    fi = max(an)
    ans = []
    for i in range(len(an)):
        if fi == an[i]:
            ans.append(i+1)
    return ans
# 다른 풀이
# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []

#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1

#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)

#     return result