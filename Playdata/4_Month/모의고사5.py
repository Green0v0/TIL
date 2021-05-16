"""
    # 첫번째(me)가 골랐을 때는 연속되도록 변경
    # 두번째가 골랐을 때는 분리
goldVaules = [2,1,3,1,2,1,8,1]
first_idx = goldVaules.index(max(goldVaules))
print(first_idx)
new_g = goldVaules[first_idx+1:]+goldVaules[:first_idx]
print(new_g)
second_idx = new_g.index((max((new_g))))
print(second_idx)

result = []
result.append(new_g[:second_idx])
result.append(new_g[second_idx+1:])
print(result)
"""
# 틀림
# 처음만 한그룹으로 이후는 그냥 나눠짐
def solution(goldValues):
    A = [goldValues]
    B = []
    A_result = 0
    B_result = 0
    check = True
    while A or B:
        if A_result == 0:
            first_idx = goldValues.index(max(goldValues))
            A_result += max(goldValues)
            B = [goldValues[first_idx+1:]+goldValues[:first_idx]]
            # if not B[0]:
            #     break
            A = []
            check = False
        if check:
            for li in A:
                idx = li.index(max(li))
                A_result += max(li)
                if li[:idx]:
                    B.append(li[:idx])
                if li[idx+1:]:
                    B.append(li[idx+1:])
            A = []
            check = False
        else:
            for li in B:
                idx = li.index(max(li))
                B_result += max(li)
                if li[:idx]:
                    A.append(li[:idx])
                if li[idx+1:]:
                    A.append(li[idx+1:])
            B = []
            check = True
    return A_result
# print(solution([5,2,1,4,3,1]))
# print(solution([1,2,1]))
# print(solution([2,1,3,1,2,1,8,1]))
# print(solution([1,2]))
# print(solution([3,1,2]))
# print(solution([1,4,2,3]))
# print(solution([1,4,5,2,3]))
# print(solution([1,5,6,2,3,4]))
# print(solution([1,4,5,6,2,3,7]))
# print(solution([1,2,3,7,8,4,5,6]))
print(solution([1,2,6,9,3,5,8,4,7]))
# print(solution([1,2,6,9,3,5,8,8,4,7]))
