# 조건, 점수 X점 이상
""" cpp, java, python / backend, frontend / junior, senior / chicken, pizza"""
# 첫 풀이
# def check(target, recruit):
#     for i,j in zip(target, recruit):
#         if i == '-':
#             continue
#         if i.isdigit() and int(i) <= int(j):
#             continue
#         if i == j:
#             continue
#         else:
#             return False
#     return True
#
# def solution(info, query):
#     cnt = 0
#     answer = []
#     for qu in query:
#         target = list(map(lambda x: x.strip(), qu.split('and')))
#         target.extend(target.pop().split())
#         for inf in info:
#             recruit = inf.split(' ')
#             if check(target, recruit):
#                 cnt += 1
#         answer.append(cnt)
#         cnt = 0
#     return answer
def solution(info, query):
    cnt = 0
    answer = []
    for q in query:
        li_q = q.replace('and', '').split()
        for i in info:
            li_i = i.split()
            if (li_q[0] != '-' and li_i[0] != li_q[0]) or (li_q[1] != '-' and li_i[1] != li_q[1]) or (li_q[2] != '-' and li_i[2] != li_q[2]) or (li_i[3] != li_q[3] and li_q[3] != '-'):
                continue
            if li_q[4] <= li_i[4]:
                cnt += 1

        answer.append(cnt)
        cnt = 0
    return answer
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))