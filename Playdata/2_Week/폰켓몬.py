def solution(nums):
    distinct = len(list(set(nums)))
    if distinct > len(nums) // 2:
        return len(nums) // 2
    else:
        return distinct

def solution2(nums):
    distinct = len(list(set(nums)))
    return distinct if distinct < len(nums) // 2 else len(nums) // 2

def solution3(nums):
    return min(len(nums) / 2, len(set(nums)))