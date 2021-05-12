import sys
T = int(sys.stdin.readline().rstrip())
people = []
for i in range(T):
    x,y = map(int,sys.stdin.readline().split())
    people.append([x,y])
# 비교함수
def rank(list):
    result = 1
    for i in range(len(people)):
        if list[0] < people[i][0] and list[1] < people[i][1]:
            result += 1
    return result

for i in range(T):
    print(rank(people[i]),end=' ')