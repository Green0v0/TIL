from itertools import combinations

def solution(nums):
    answer = 0
    # add_nums = list(map(sum,list(combinations(nums,3))))
    for x, y, z in combinations(nums,3):
        xyz = x + y + z
        for i in range(2, xyz):
            if xyz % i == 0:
                break
            # if i == xyz - 1:
            #     answer += 1
        # for-else문 사용
        else:
            answer += 1

    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))

# 다른 풀이
def prime_number(x):
    answer = 0
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            answer+=1
    return 1 if answer==1 else 0

def solution1(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums,3)])