import sys
from collections import Counter
n = int(sys.stdin.readline().rstrip())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline().rstrip()))
nums = sorted(nums)
cou = Counter(nums)
new_nums = sorted(cou.items(), key=lambda x: (-x[1], x[0]))
da, result, c = new_nums[0][1], 0, 0 # 최빈
for value, cnt in new_nums:
    if c == 2:
        break
    if cnt == da:
        c += 1
        result = value

print(int(round(sum(nums)/len(nums),0)))
print(nums[len(nums)//2])
print(result)
print(nums[-1] - nums[0])