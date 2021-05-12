from itertools import combinations
# def solution(relation):
#     col = list(zip(*relation))
#     candidate = []
#     other = list(range(len(relation[0])))
#     cnt = 0
#     for i in range(len(col)):
#         if len(col[i]) == len(list(set(col[i]))):
#             candidate.append(i)
#             other.pop(i)
#             cnt += 1
#
#     for i in range(2,len(relation[0])):
#         cols = list(combinations(other,i))
#
#         for x in cols: # (1,2) (1,3) ... (1, 2, 3)
#             target_col = []
#             for j in x:
#                 target_col.append(list(col[j]))
#             result = list(zip(*target_col))
#             if len(result) == len(list(set(result))):
#                 candidate.extend(list(x))
#                 other = list(set(other) - set(candidate))
#                 cnt += 1
#     return cnt

# from itertools import combinations
# # 원소들이 모두 유니크한지 확인해주는 함수
# def uniq(li):
#     if len(li) == len(list(set(li))):
#         return True
#
# def col(li):
#     col = list(zip(*li))
#     return col
#
# def solution(relation):
#     for i in range(len(relation[0])):
#         test = col(relation[i])
#         if uniq(test):
#             print(i, test)

# for i in range(len(col)):
#         if len(col[i]) == len(list(set(col[i]))):
#             candidate.append(i)
#             other.pop(i)
#             cnt += 1
def checkuniq(arr, row):
    return True if len(set(zip(*arr))) == row else False


def checkmin(num, unique):
    for i in unique:
        if i & num == i: return False
    return True


def solution(relation):
    relation = tuple(zip(*relation))
    col = len(relation)
    row = len(relation[0])
    candidate = []

    for num in range(1, 1 << col):
        tmp = tuple(relation[i] for i in range(col) if num & (1 << i))
        if checkuniq(tmp, row) and checkmin(num, candidate):
            candidate.append(num)

    return len(candidate)

def solution(relation):
    answer_list = list()
    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)

        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                if (num & i) == num:
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)
    return len(answer_list)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))