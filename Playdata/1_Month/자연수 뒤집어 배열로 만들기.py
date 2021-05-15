def solution(n):
    answer = []
    while n>0:
        answer.append(n%10)
        n = n//10
#return [int(i) for i in str(n)][::-1]
#return list(map(int, reversed(str(n))))
    return answer