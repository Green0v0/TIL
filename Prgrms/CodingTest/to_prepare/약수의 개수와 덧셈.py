def solution(left, right):
    result = 0
    for num in range(left, right + 1):
        cnt= 0
        for n in range(1, num+1):
            if num % n == 0:
                cnt += 1
        result += num if cnt % 2 == 0 else -num

    return result

print(solution(13,17))