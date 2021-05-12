from collections import deque

def solution(skill, skill_trees):
    cnt = 0
    for s in skill_trees:
        sk = deque(skill)
        for i in s:
            if i in skill and i != sk.popleft():
                break
        else:
            cnt += 1

    return cnt


print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))