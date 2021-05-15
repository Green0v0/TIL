# 책 넣기
# from collections import deque
def solution(weights,maxWeight):
    cnt = 1
    check = maxWeight
    if not weights:
        return 0
    for i in weights:
        if check-i< 0:
            cnt+=1
            check = maxWeight - i
            continue
        check = check-i
    return cnt

print(solution([1,1,1,7,7,7],8))
print(solution([1],1))
print(solution([],1))
print(solution([1,15,1,15,1,15,1,15,1,15],15))

# 해설
class Solution:
    def solution(self, weights, maxWeight):
        temp = 0
        result = 0

        for i in weights:
            if temp + i > maxWeight:
                result += 1
                temp = i
            else:
                temp += i

        if temp > 0:
            result += 1

        return result

class Solution:
    def solution(self, weights, maxWeight):
        self.weights = weights
        self.maxWeight = maxWeight

        box = []
        suma = 0
        for i, v in enumerate(self.weights):
            if suma < self.maxWeight:
                suma += v
                if i < len(self.weights) - 1:
                    if self.weights[i + 1] + suma > self.maxWeight:
                        box.append(suma)
                        suma = 0
                else:
                    box.append(suma)

        return len(box)

