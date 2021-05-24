# def solution(distance=25, rocks=[2, 14, 11, 21, 17], n=2):
    # return이 4
distance=25
rocks=[2, 14, 11, 21, 17]
# print(type(rocks))
n=2
answer = 0
def count(mid):
    cnt=0
    ep=0
    small=0
    for i in range(n+1):
        if rocks[i]-ep>=mid:
            len=rocks[i]-ep
            small=min(small,len)
            cnt+=1
            ep=rocks[i]
    return cnt,small
# distance=distance
# n=n
# rocks=rocks
tmp=len(rocks)-n
# print(rocks)
rocks.append(distance)
rocks.sort()
lt=0
rt=distance
print(count(12))
# while lt<=rt:
#     mid=(lt+rt)//2
#     print(mid)
#     if count(mid)>=tmp:
#         # print()
#         answer=mid
#         lt=mid+1
#     else:
#         rt=mid-1
# print(answer)
    # return answer
# 출발지점부터 도착지점까지의 거리 distance
# 바위들이 있는 위치를 담은 배열 rocks
# 제거할 바위의 수 n이 매개변수로 주어질 때
# 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값을 return