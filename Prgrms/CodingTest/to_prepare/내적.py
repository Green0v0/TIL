def solution(a, b):
    answer = sum(map(lambda x: x[0]*x[1], zip(a,b)))
    return answer

print(solution([1,2,3,4],[-3,-1,0,2]))
print(solution([-1,0,1],[1,0,-1]))