import sys

score = []
sum_score = 0
for i in range(5):
    # score.append(int(sys.stdin.readline().rstrip()))
    score = int(sys.stdin.readline().rstrip())
    if score < 40 :
        score = 40
    sum_score = sum_score + score
    avg_score = sum_score // (i+1)

print(avg_score)