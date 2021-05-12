def solution(n, lost, reserve):
    student = [1 for _ in range(n)]
    for l in lost:
        student[l-1] -=1
    for r in reserve:
        student[r-1] +=1
    print(student)
    if 0 not in student:
        # return n
        pass
        # print(n)
    # 0이 있다면
    else:
        # 전위, 후위 구분후 비교 => 큰 값을 return
        # lt, rt rt는 0이 아니면 +=1 0이면 lt가 rt-1로 이동
        # lt는 abs(lt-rt) == 1 and lt값이 2일 때인 조건
        lt = 0
        rt = 0
        while True:
            if rt >= n or lt >= n:
                break
            if student[rt] != 0:
                rt += 1
            else:
                if abs(lt - rt) == 1 and student[lt] == 2:
                    student[rt] = 1
                    student[lt] = 1
                else:
                    lt += 1
                    if lt-rt>=2:
                        rt+=1
    # return n-student.count(0)
    print(student)
    print(n-student.count(0))

# solution(8,[3, 4, 7, 8],[1, 2, 3, 4, 5, 7, 8])#5
solution(8,[4,7],[6])#7
# solution(5,[1,3],[2,4,5])#5
# solution(5,[2,4],[3])#4
# solution(5,[3],[1])#2
# print('check')
# solution(3,[1,2],[2,3])#2
# solution(5,[2,4],[2,4,5])#2
# solution(8,[1,2,4,6],[1,2,4,6])#8

# 다른 사람 풀이
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    for i in new_lost:
        if i + 1 in new_reserve:
            new_reserve.remove(i + 1)
        elif i - 1 in new_reserve:
            new_reserve.remove(i - 1)
        else:
            n-=1
    return n
