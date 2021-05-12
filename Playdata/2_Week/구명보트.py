def solution(people, limit):
    people.sort()
    lt, rt = 0, len(people)-1
    # result = 0
    cnt = 0
    while True:
        result = people[lt] + people[rt]
        if result > limit:
            rt -= 1
            cnt += 1
        else:
            lt += 1
            rt -= 1
            cnt += 1

        if lt == rt:
            cnt += 1
            break

        if lt > rt:
            break

    return cnt

print(solution([70,50,80,50],100))
print(solution([70,50,20,20,20,80,50],100))
print(solution([70,80,50],100))
# print(solution([70],100))

# 다른 사람 풀이
def othersolution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer