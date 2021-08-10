"""
3
9
7 4 2 0 0 6 0 7 0
9
7 4 2 0 0 6 7 7 0
20
52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53
"""
n = int(input())
for i in range(n):
    length = int(input())
    box = list(map(int, input().split()))
    result = []
    for idx in range(len(box) - 1):
        cnt = 0
        for b in range(idx + 1,len(box)):
            cnt += 1
            if box[idx] > box[b]:
                continue
            else:
                break
        result.append(cnt)
    print(max(result))