# bfs? Greedy?
def solution(n, costs):
    costs = sorted(costs, key= lambda x:x[2])
    # print(costs)
    s = set()
    answer = 0
    for x, y, v in costs:
        # 수정 필요
        s.add(x)
        s.add(y)
        answer += v
        if len(list(s)) == n:
            # print(x,y,v)
            break

    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	))