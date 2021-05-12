import sys
N = int(sys.stdin.readline().rstrip())
li = list(map(int,sys.stdin.readline().split()))
# 평균값
avg = round(sum(li)/N,0)
# 평균과의 차이값 리스트
a = list(range(N))
for i in range(len(li)):
    a[i] = abs(li[i] - avg)
# 차이의 최소값
min_a = min(a)

# 최소값이 동일한 값들의 index
# print([i for i,j in enumerate(a) if j==min_a])
li_index = [i for i,j in enumerate(a) if j==min_a]
# 조건 1 차이가 동일 시 점수가 높은 학생
# 조건 2 차이가 동일하고 점수가 같을 시 번호가 빠른 학생
# li_index = [1,6,8]
final_li = []
for i in li_index:
    final_li.append([i,li[i]])
# [[1, 73], [6, 75], [8, 75]]

final_index = []
for i in range(len(final_li)):
    max_an = max(final_li,key=(lambda x : x[1]))
    if final_li[i][1] == max_an[1]:
        final_index.append(final_li[i][0])
# print(max_an)
# print(final_index)
min_index = min(final_index)

print(int(avg), min_index+1)
# 답은 74, 7번 째

