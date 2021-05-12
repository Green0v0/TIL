from math import ceil
def solution(progresses, speeds):
    progress = []
    for i in range(len(progresses)):
        progress.append(ceil((100 - progresses[i]) / speeds[i]))

    stack = []
    result = []
    cnt = 1
    for q in progress:
        if not stack:
            stack.append(q)
            continue

        if stack[-1] >= q:
            cnt += 1

        else:
            stack.pop()
            stack.append(q)
            result.append(cnt)
            cnt = 1

    if stack:
        result.append(cnt)

    return result

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99]	,[1, 1, 1, 1, 1, 1]	))
print(solution([95],[1]))

# 다른 사람 풀이
def solution1(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

# 내 다른 풀이
from math import ceil
def solution2(progresses,speeds):
    answer = []
    new = []
    # 리스트 컴프리헨션
    for x in range(len(progresses)):
        new.append(ceil((100 - progresses[x])/speeds[x]))

    v = new[0]
    cnt = 0
    for i in range(len(progresses)):
        if v >= new[i]:
            cnt+=1
            continue
        answer.append(cnt)
        v = new[i]
        cnt=1

    answer.append(cnt)
    return answer