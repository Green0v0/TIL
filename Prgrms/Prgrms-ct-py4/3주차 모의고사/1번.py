def isprime(n):
    check = [False, False] + [True] * (n - 1)
    for i in range(int(n // 2) + 1):
        if check[i]:
            for j in range(i * i, n + 1, i):
                check[j] = False
    return check[n]

def solution(nums):
    answer = 0
    len_nums = len(nums)
    for i in range(len_nums):
        for j in range(i + 1, len_nums):
            for k in range(j + 1, len_nums):
                if isprime(nums[i] + nums[j] + nums[k]):
                    answer += 1
    return answer

print(solution([1,2,3,4]))