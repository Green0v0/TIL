# 둥근 길
# 횟수를 새는 cnt
# 값을 측정하는 present
def solution(self, width, length):
    # 계산할 때 필요하므로 새로 변수를 생성
    w = width
    l = length - 1
    # 회전할 횟수를 계산
    cnt = w + l
    # 좌표계산
    present = [width - 1, length - 1]
    # 나선형 회전 없이 바로 도착할 경우
    if width == 1:
        return present
    # +와 -를 번갈아서 하기 위한 변수 check
    check = False
    while True:
        if cnt == width * length:
            break
        w -= 1
        l -= 1
        cnt += (w + l)
        if check == True:
            present[0] += w
            present[1] += l
            check = False
        else:
            present[0] -= w
            present[1] -= l
            check = True

    return present
print(solution(1,11))
print(solution(12,50))
print(solution(50,50))
print(solution(2,4))
print(solution(10,10))

# 해설
def solution(self, width, length):
    # width와 length의 최솟값과 최댓값을 저장합니다.
    minNum = min(width, length)
    maxNum = max(width, length)

    # 최솟값을 반으로 나눈 값과 최댓값에서 그 값을 뺀 값을 저장합니다.
    n = int(minNum / 2)
    cal = maxNum - n

    if width > length:
        if (length % 2 == 1):
            return [cal - 1, n]

    else:
        if (width % 2 == 1):
            return [n, cal - 1]

    return [n - 1, n]