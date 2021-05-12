# 1초에 1만큼 움직임
# 올라온 시간 + 2초(길이 2인 다리) = 다리를 지닌 트럭에 추가된 시간
from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    in_bridge = deque()
    time = 0
    # 트럭무게, 다리를 건너는 시간 계산 값, 시작값
    while True:
        time += 1
        result = sum(map(lambda x: x[0], in_bridge))
        if truck_weights and result + truck_weights[0] <= weight:
            in_bridge.append([truck_weights.popleft(), 0, time])
            for i in in_bridge:
                i[1] += 1
        else:
            for i in in_bridge:
                i[1] += 1

        if in_bridge[0][1] >= bridge_length:
            in_bridge.popleft()

        if not truck_weights:
            time += bridge_length
            break

    # print(time)
    return time

print(solution(2,10,[7,4,5,6])) #8
# print(solution(100,100,[10])) #101
# print(solution(100,100,[10,10,10,10,10,10,10,10,10,10])) #110

# 다른사람 풀이
def solution1(bridge_length, weight, truck_weights):
    q=[0]*bridge_length
    sec=0
    while q:
        sec+=1
        q.pop(0)
        if truck_weights:
            if sum(q)+truck_weights[0]<=weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return sec